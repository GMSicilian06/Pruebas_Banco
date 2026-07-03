import cProfile
import random
import sys
import time


SIZE = 1000  # size of the square matrices


def generate_matrix():
    """
    Generate a SIZE x SIZE matrix (list of lists) with random integers
    between 0 and 9.
    """
    matrix = [[0] * SIZE for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            matrix[i][j] = random.randint(0, 9)
    return matrix


def multiply_matrices(matrix_a, matrix_b):
    """
    Perform standard (cubic-time) matrix multiplication (A * B = C).
    """
    result_matrix = [[0] * SIZE for _ in range(SIZE)]

    for i in range(SIZE):           # rows of the result matrix (i)
        for j in range(SIZE):       # columns of the result matrix (j)
            for k in range(SIZE):   # columns of A and rows of B (k)
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
                # C[i][j] += A[i][k] * B[k][j], this line involves:
                #   three Python integer lookups
                #   one multiplication
                #   one addition
                #   one assignment

    return result_matrix


def main():
    A = generate_matrix()
    B = generate_matrix()
    C = multiply_matrices(A, B)

    checksum = 0
    for i in range(SIZE):
        checksum += sum(C[i])
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
