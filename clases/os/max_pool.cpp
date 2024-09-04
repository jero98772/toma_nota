#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Function to apply max pooling on the image
vector<vector<int>> maxPooling(const vector<vector<int>>& image, int poolSize) {
    int height = image.size();
    int width = image[0].size();
    int newHeight = height / poolSize;
    int newWidth = width / poolSize;

    vector<vector<int>> pooledImage(newHeight, vector<int>(newWidth, 0));

    for (int i = 0; i < newHeight; ++i) {
        for (int j = 0; j < newWidth; ++j) {
            int maxVal = 0;
            for (int m = 0; m < poolSize; ++m) {
                for (int n = 0; n < poolSize; ++n) {
                    int row = i * poolSize + m;
                    int col = j * poolSize + n;
                    if (row < height && col < width) {
                        maxVal = max(maxVal, image[row][col]);
                    }
                }
            }
            pooledImage[i][j] = maxVal;
        }
    }

    return pooledImage;
}

// Function to print the image
void printImage(const vector<vector<int>>& image) {
    for (const auto& row : image) {
        for (const auto& pixel : row) {
            cout << pixel << " ";
        }
        cout << endl;
    }
}

int main() {
    // Example image (4x4)
    vector<vector<int>> image = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    int poolSize = 2; // Size of the pooling filter (2x2)
    vector<vector<int>> pooledImage = maxPooling(image, poolSize);

    cout << "Original Image:" << endl;
    printImage(image);

    cout << "Pooled Image (with max pooling filter):" << endl;
    printImage(pooledImage);

    return 0;
}
