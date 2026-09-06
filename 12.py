import numpy as np

class matrix:
    def __init__(self, n):
        self.n = n
        self.A = []

    def matrix1(self):

        for i in range(self.n):

            row = []

            for j in range(self.n):

                value = int(input(f"Enter the value for A[{i}][{j}]: "))

                row.append(value)

            self.A.append(row)


matrixA = matrix(4)

matrixA.matrix1()

A = np.array(matrixA.A)

print("\nMatrix:")
print(A)


# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)