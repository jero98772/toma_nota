#include <opencv2/opencv.hpp>
#include <omp.h>
#include <iostream>
#include <vector>

using namespace cv;
using namespace std;

// Define the structure for a Haar-like feature
struct HaarFeature {
    int type; // Type of feature
    Rect rect1, rect2; // Two rectangles of the feature

    // Compute the value of the feature in a given integral image
    double compute(const Mat& integralImg) const {
        double sum1 = integralImg.at<int>(rect1.y + rect1.height, rect1.x + rect1.width) -
                      integralImg.at<int>(rect1.y + rect1.height, rect1.x) -
                      integralImg.at<int>(rect1.y, rect1.x + rect1.width) +
                      integralImg.at<int>(rect1.y, rect1.x);

        double sum2 = integralImg.at<int>(rect2.y + rect2.height, rect2.x + rect2.width) -
                      integralImg.at<int>(rect2.y + rect2.height, rect2.x) -
                      integralImg.at<int>(rect2.y, rect2.x + rect2.width) +
                      integralImg.at<int>(rect2.y, rect2.x);

        return sum2 - sum1;
    }
};

// Pre-compute the integral image for fast feature calculation
Mat computeIntegralImage(const Mat& img) {
    Mat integralImg;
    integral(img, integralImg, CV_32S);
    return integralImg;
}

// Detect face using the trained cascade classifier with OpenMP
vector<Rect> detectFaces(const Mat& img, const vector<HaarFeature>& cascade) {
    vector<Rect> faces;
    Mat integralImg = computeIntegralImage(img);

    // Parallelizing the sliding window detection using OpenMP
    #pragma omp parallel for collapse(2) schedule(dynamic)
    for (int y = 0; y < img.rows - 24; y += 2) {
        for (int x = 0; x < img.cols - 24; x += 2) {
            bool passed = true;

            // Apply cascade of Haar features
            for (const auto& feature : cascade) {
                double featureVal = feature.compute(integralImg);
                if (featureVal < 0) { // Threshold (this is simplified for demo)
                    passed = false;
                    break;
                }
            }

            // If passed, this is a face
            if (passed) {
                #pragma omp critical
                faces.push_back(Rect(x, y, 24, 24));
            }
        }
    }
    return faces;
}

int main() {
    // Load the image
    Mat img = imread("2.jpg", IMREAD_GRAYSCALE);
    if (img.empty()) {
        cout << "Could not load image!" << endl;
        return -1;
    }

    // Define a simple cascade of Haar-like features
    vector<HaarFeature> cascade;
    cascade.push_back({0, Rect(1, 1, 12, 12), Rect(13, 1, 12, 12)});
    // You can add more features for better accuracy

    // Detect faces
    vector<Rect> faces = detectFaces(img, cascade);

    // Display results
    for (const auto& face : faces) {
        rectangle(img, face, Scalar(255, 0, 0), 2);
    }

    imshow("Detected Faces", img);
    waitKey(0);
    return 0;
}
