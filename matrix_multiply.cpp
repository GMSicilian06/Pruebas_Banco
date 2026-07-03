#include <cstdlib>
#include <ctime>
#include <iostream>
#include <numeric>


const int SIZE = 1000;  // size of the square matrices


// generate and fill a matrix with random integers (0-9)
void generateMatrix(int matrix[SIZE][SIZE]) {
    static bool seeded = false;
    if (!seeded) {
        std::srand(std::time(0));
        seeded = true;
    }
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            matrix[i][j] = std::rand() % 10;
        }
    }
}


// multiply matrixA and matrixB and store the result in resultMatrix
void multiplyMatrices(
    const int matrixA[SIZE][SIZE],
    const int matrixB[SIZE][SIZE],
    volatile int resultMatrix[SIZE][SIZE]
) {
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            resultMatrix[i][j] = 0;
            for (int k = 0; k < SIZE; ++k) {
                resultMatrix[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }
}


int main() {
    // move these 16 MB variables off the stack and into static memory
    // to prevent a stack overflow segmentation fault
    static int A[SIZE][SIZE];
    static int B[SIZE][SIZE];

    // keep `volatile` to prevent compiler from optimizing the math
    static volatile int C[SIZE][SIZE];

    // generate random values for A and B
    generateMatrix(A);
    generateMatrix(B);

    // perform the matrix multiplication
    multiplyMatrices(A, B, C);

    long long checksum = 0;
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            checksum += C[i][j];
        }
    }
    std::cerr << "checksum = " << checksum << std::endl;

    return 0;
}
