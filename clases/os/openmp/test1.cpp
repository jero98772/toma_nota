#include <iostream>
#include <omp.h>
#include <vector>
#include <numeric>  // For std::accumulate

int main() {
    const int N = 1000000;
    std::vector<int> array(N);

    // Initialize the array with values from 1 to N
    #pragma omp parallel for
    for (int i = 0; i < N; ++i) {
        array[i] = i + 1;
    }

    // Calculate the sum of the array in parallel
    long long sum = 0;

    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < N; ++i) {
        sum += array[i];
    }

    std::cout << "The sum of the array elements is: " << sum << std::endl;

    return 0;
}
