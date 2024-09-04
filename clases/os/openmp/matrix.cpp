#include <iostream>
#include <vector>
#include <omp.h>

int main() {
    const int N = 500;  // Size of the matrices
    std::vector<std::vector<int>> A(N, std::vector<int>(N));
    std::vector<std::vector<int>> B(N, std::vector<int>(N));
    std::vector<std::vector<int>> C(N, std::vector<int>(N, 0));

    // Initialize matrices A and B with some values
    #pragma omp parallel for collapse(2)
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            A[i][j] = i + j;
            B[i][j] = i - j;
        }
    }

    // Perform matrix multiplication C = A * B
    #pragma omp parallel for collapse(2)
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            for (int k = 0; k < N; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    // Print a small part of the resulting matrix for verification
    std::cout << "C[0][0] = " << C[0][0] << std::endl;
    std::cout << "C[N-1][N-1] = " << C[N-1][N-1] << std::endl;

    return 0;
}
