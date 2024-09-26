#include "StdAfx.h"
#include "Cascade.h"
#include "Image.h"
#include "AdaBoost.h"
#include <opencv2/opencv.hpp>
#include "ViolaJones.h"  // Include your ViolaJones class header

#include "ImageLoader.h"
#include <list>
#include <vector>
#include <iostream>
using namespace std;

/*
 * Class implementing the Viola-Jones algorithm and creating a cascade
 *
 * @author: Ivan Kusalic
 */
class ViolaJones {
public:
    vector<Image*> positiveTest;  // Set of positive integral images for testing
    vector<Image*> negativeTest;  // Set of negative integral images for testing
    
    ImageLoader &negativeTestLoader, &positiveTestLoader;

    int minNumber; // Minimum number of negative test examples at any time

    int clearedNegativeTestSize; // Number of negative examples cleared for memory efficiency

    ~ViolaJones(void) {}

    // Constructor for initialization:
    ViolaJones(ImageLoader &positiveTestLoader, ImageLoader& negativeTestLoader, int minNumber);

    /*
     * f - the maximum acceptable false positive rate per layer
     * d - the minimum acceptable detection rate per layer
     * targetF - target overall false positive rate
     * cascade - the cascade being built
     */
    void buildCascade(double f, double d, double targetF, Cascade &cascade);

    // Evaluate current cascaded classifier on validation set to determine tmpF and tmpD
    pair<double,double> evaluateOnTest(Cascade &cascade);

    // For the given integral image, returns whether it is classified positively or negatively
    bool evaluate(Image *img, Cascade &cascade);

    /*
     * Evaluate the current cascaded detector on the set of non-face images
     * and put any false detections into the set N
     */
    void evaluateOnTrainNegative(vector<Image*> &N, Cascade &cascade);

    /*
     * Decrease threshold for the ith classifier until the current cascaded classifier
     * has a detection rate of at least minD (this also affects tmpF)
     *
     * Uses binary search to find the threshold
     */
    void decreaseThreshold(int ith, double minD, Cascade &cascade);

    /*
     * Function used in case of a computer error during the learning process.
     * After each newly created level of the cascade, it saves the cascade to a file temp.cascade.
     * This function reads the last level of the cascade from that file and continues learning    
     */
    void recoverFromError(int &i, double &lastD, double &lastF, vector<Image*> &N);

    /*
     * Clears data resulting from temporary storage for recovery from an error.
     */
    void clearTempData();

    /*
     * Saves data important for continuing the learning process to disk in files: podaci.temp, temp.cascade
     */
    void saveData(Cascade cascade, int &i, double &lastD, double &lastF);
};

#define MAX 1000000000
#define debug(x) cout << #x << ": " << x << endl;

ViolaJones::ViolaJones(ImageLoader &positiveTestLoader, ImageLoader& negativeTestLoader, int minNumber)
    : negativeTestLoader(negativeTestLoader), positiveTestLoader(positiveTestLoader), minNumber(minNumber), clearedNegativeTestSize(0) {
    positiveTest = positiveTestLoader.loadNextImages();
    negativeTest = negativeTestLoader.loadNextImages();
}

/*
 * f - the maximum acceptable false positive rate per layer
 * d - the minimum acceptable detection rate per layer
 * targetF - target overall false positive rate
 * cascade - the cascade being built
 */
void ViolaJones::buildCascade(double f, double d, double targetF, Cascade &cascade) {
    // P - set of positive examples; N - set of negative examples:
    vector<Image*> P(positiveTest.begin(), positiveTest.end());
    vector<Image*> N(negativeTest.begin(), negativeTest.end());    

    double tmpF = 1.0;  // Current false positive rate
    double lastF = 1.0;  // False positive rate of the previous level
    double tmpD = 1.0;  // Current detection rate
    double lastD = 1.0;  // Detection rate of the previous level
    
    int i = -1;  // Level of the cascade
    int n;  // Number of features in the current level of the cascade
    
    pair<double,double> tmpRet;  // Helper variable

    recoverFromError(i, lastD, lastF, N); // Recover from error if the previous learning process was interrupted by a computer error

    while (tmpF > targetF) {
        cout << "Cascade level: " << i + 2 << ". " << "Number of features: " << P.size() << " " << "Number of non-features: " << N.size() << " " << endl;
        i++;
        n = 0;
        tmpF = lastF;
                
        cascade.cascade.push_back(vector<Feature>(0)); // Add an empty vector to the end to make space for the next level of the cascade
        while (tmpF > f * lastF) {
            n += 15; // How many features to add (ideally only one, but that's slow)
            cout << "Number of features: " << n << " False positive: " << tmpF << " " << "Looking for: " << targetF << endl;

            // Train the level of the cascade with n features
            cascade.cascade[i] = AdaBoost::startTraining(P, N, Feature::generatedFeatures, n);
            cascade.levelThreshold.push_back(MAX); /////////////////////////10e6
                                    
            /*
             * Decrease threshold for the i-th classifier until the current cascaded classifier
             * has a detection rate of at least d * lastD (this also affects tmpF):
             */
            decreaseThreshold(i, d * lastD, cascade);    

            // Evaluate current cascaded classifier on validation set to determine tmpF and tmpD:
            // No validation set exists
            tmpRet = evaluateOnTest(cascade);
            
            tmpF = tmpRet.first;
            tmpD = tmpRet.second;                   

            debug(tmpF);
            debug(tmpD);
        }
        
        N.clear();
        lastD = tmpD;       
        lastF = tmpF;
        
        /*
         * If tmpF > targetF then evaluate the current cascaded detector on the set of non-face images
         * and put any false detections into the set N:
         */
        if (tmpF > targetF) evaluateOnTrainNegative(N, cascade);
        cout << "Currently have: " << negativeTest.size() << " negative examples.";
    
        saveData(cascade, i, lastD, lastF); // Save the cascade for the possibility of continuing training in case of a computer error
    }
    clearTempData(); // Clears files created by temporarily saving the cascade to disk due to the possibility of continuing the learning process
}

void ViolaJones::clearTempData() {
    system("del podaci.temp");
}

void ViolaJones::saveData(Cascade cascade, int &i, double &lastD, double &lastF) {
    cascade.saveCascade("temp.cascade");
    FILE *fout = fopen("podaci.temp", "w");
    fprintf(fout, "%lf %lf %d", lastD, lastF, i);
    fclose(fout);
}

void ViolaJones::recoverFromError(int &i, double &lastD, double &lastF, vector<Image*> &N) {
    Cascade cascade(ColorSpace::RGB); // Default value, actual value is loaded when loaded
    FILE *fin = fopen("podaci.temp", "r");
    if (fin == NULL) return;
    
    cout << "RECOVERING FROM ERROR!!! [Y=yes, N=no]" << endl;
    string choice; 
    cin >> choice;
    if (string("Yy").find(choice) != string::npos) {
        cout << endl << "Yes" << endl;
    } else {
        cout << "No" << endl;
        fclose(fin);
        return;
    }

    fscanf(fin, "%lf %lf %d", &lastD, &lastF, &i);
    fclose(fin);    
    i--; // Not sure if this is necessary
    cascade.loadCascade("temp.cascade");
    N.clear();
    evaluateOnTrainNegative(N, cascade);
}

// Evaluate current cascaded classifier on validation set to determine tmpF and tmpD
pair<double,double> ViolaJones::evaluateOnTest(Cascade &cascade) { 
    int correctP = 0, errorN = 0;  // Number of errors on P and N
    
    for (int i = 0; i < positiveTest.size(); i++)
        if (evaluate(positiveTest[i], cascade)) correctP++;
    
    for (int i = 0; i < negativeTest.size(); i++)
        if (evaluate(negativeTest[i], cascade)) errorN++;
    
    debug(positiveTest.size());
    debug(negativeTest.size());
    debug(correctP);
    debug(errorN);
    
    return make_pair(errorN / (double)(negativeTest.size() + clearedNegativeTestSize), 
                     correctP / (double)positiveTest.size()); // ?????????????
}

// For the given integral image, returns whether it is classified positively or negatively
bool ViolaJones::evaluate(Image *img, Cascade &cascade) {
    double sum = 0;

    for (int k, j, i = 0; i < cascade.cascade.size(); i++) {
        sum = 0;  // Sum for the currently processed level of the cascade

        for (k = 0; k < cascade.cascade[i].size(); k++) {
            sum += cascade.cascade[i][k].evaluate(img); // Evaluate feature
        }
        if (sum < cascade.levelThreshold[i]) return false; // If the threshold is not met, return false
    }
    return true; // If all levels return true, return true
}

/*
 * Evaluate the current cascaded detector on the set of non-face images
 * and put any false detections into the set N
 */
void ViolaJones::evaluateOnTrainNegative(vector<Image*> &N, Cascade &cascade) {
    cout << "Evaluating on negative set (N)... " << endl;
    for (int i = 0; i < negativeTest.size(); i++) {
        if (evaluate(negativeTest[i], cascade)) {
            N.push_back(negativeTest[i]); // Add false detections to N
            clearedNegativeTestSize++; // Increase the count of cleared negatives
        }
    }
    cout << "Finished evaluation on negative set (N). Size of N: " << N.size() << endl;
}

/*
 * Decrease threshold for the ith classifier until the current cascaded classifier
 * has a detection rate of at least minD (this also affects tmpF)
 *
 * Uses binary search to find the threshold
 */
void ViolaJones::decreaseThreshold(int ith, double minD, Cascade &cascade) {
    int low = 0, high = cascade.cascade[ith].size() - 1, mid;
    int position = 0;

    while (low <= high) {
        mid = (low + high) / 2; // Middle value for binary search
        cascade.levelThreshold[ith] = cascade.cascade[ith][mid].threshold;

        pair<double,double> ret = evaluateOnTest(cascade); // Get false positive and detection rates

        if (ret.second >= minD) { // If detection rate is met
            position = mid; // Set position to mid
            high = mid - 1; // Search lower half
        } else {
            low = mid + 1; // Search upper half
        }
    }

    cascade.levelThreshold[ith] = cascade.cascade[ith][position].threshold; // Set the threshold to the best position found
}



using namespace std;
using namespace cv;

int main(int argc, char** argv) {
    if (argc != 2) {
        cout << "Usage: " << argv[0] << " <image_path>" << endl;
        return -1;
    }

    // Load the image
    Mat image = imread(argv[1]);
    if (image.empty()) {
        cout << "Could not open or find the image!" << endl;
        return -1;
    }

    // Convert the image to integral image if necessary
    // (You may need to implement this based on your Image class)
    ImageLoader positiveLoader("path/to/positive/images"); // Provide the path
    ImageLoader negativeLoader("path/to/negative/images"); // Provide the path
    ViolaJones detector(positiveLoader, negativeLoader, 50); // Initialize the detector

    Cascade cascade(ColorSpace::RGB); // Define the color space
    detector.buildCascade(0.5, 0.7, 0.01, cascade); // Build the cascade

    // Detect faces
    Image* img = new Image(image); // Assuming you have an Image constructor that takes cv::Mat
    if (detector.evaluate(img, cascade)) {
        cout << "Face detected!" << endl;
        // Draw rectangle around the detected face (if any processing is required)
    } else {
        cout << "No face detected!" << endl;
    }

    // Clean up
    delete img;

    return 0;
}
