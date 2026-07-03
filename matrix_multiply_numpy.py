import cProfile
import random
import sys
import time
import numpy as np


SIZE = 1000  # size of the square matrices


def generate_numpy_matrix():
    """
    Generate a SIZE x SIZE NumPy array of random integers between 0 and 9.
    """
    # use numpy's random integer generation for speed
    # dtype=np.int32 ensures we use a fixed-size integer type
    # similar to `int` in c++
    return np.random.randint(0, 10, size=(SIZE, SIZE), dtype=np.int32)


def multiply_matrices_numpy(matrix_a, matrix_b):
    """
    Perform matrix multiplication using NumPy's dot product operator @.
    This operation is highly optimized and vectorized.
    """
    return matrix_a @ matrix_b


def main():
    A = generate_numpy_matrix()
    B = generate_numpy_matrix()
    C = multiply_matrices_numpy(A, B)

    checksum = np.sum(C)
    print(f"{checksum = }")


########################################
# test runtime
########################################


random.seed(time.time())


# without profiling
start = time.time()
main()
end = time.time()
print(f"total time = {end - start:.5f} seconds")


# with profiling
# profiler = cProfile.Profile()
# profiler.enable()
# main()
# profiler.disable()
# profiler.print_stats()
