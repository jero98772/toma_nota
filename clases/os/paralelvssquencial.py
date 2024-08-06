import time
from functools import wraps
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count
import random

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to execute.")
        return result
    return wrapper


@measure_time
def fftp(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[::2])
    odd = fft(x[1::2])
    
    def worker(k):
        return np.exp(-2j * np.pi * k / N) * odd[k]
    
    with ThreadPoolExecutor() as executor:
        T = list(executor.map(worker, range(N // 2)))
    
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

@measure_time
def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[::2])
    odd = fft(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]



# Example usage
@measure_time
def example_function(x):
    time.sleep(2)  # Simulate a delay
    return x ** 2


@measure_time
def sequential_matrix_multiply(A, B):
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape

    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B")

    C = np.zeros((rows_A, cols_B))

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    
    return C



def multiply_row_by_column(args):
    A, B, row, col = args
    return sum(A[row, k] * B[k, col] for k in range(A.shape[1]))

@measure_time
def parallel_matrix_multiply(A, B):
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape

    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B")

    C = np.zeros((rows_A, cols_B))

    with Pool(cpu_count()) as pool:
        args = [(A, B, i, j) for i in range(rows_A) for j in range(cols_B)]
        results = pool.map(multiply_row_by_column, args)
        for idx, value in enumerate(results):
            row = idx // cols_B
            col = idx % cols_B
            C[row, col] = value

    return C

#result = example_function(5)
#print(f"Result: {result}")
#x = np.random.random(10)
#print("Input:", x)
#print("FFT:", fft(x))

#print("Input:", x)
#print("FFT paralelized:", fftp(x))

np.random.seed(0)  # For reproducibility

s=300#random.randint(0,50)
A = np.random.randint(0, 10, (s, s))
B = np.random.randint(0, 10, (s, s))

# Perform matrix multiplication
C_sequential = sequential_matrix_multiply(A, B)
C_parallel = parallel_matrix_multiply(A, B)

print(s)
# Print the matrices and results
print("Matrix A:")
#print(A)
print("\nMatrix B:")
#print(B)
print("\nResult of Sequential Matrix Multiplication:")
#print(C_sequential)
print("\nResult of Parallel Matrix Multiplication:")
#print(C_parallel)