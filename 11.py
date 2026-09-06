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

B = np.array(matrixA.A)

print("\nMatrix:")
print(B)

det = np.linalg.det(B)
print("\nDeterminant:", det)

rank = np.linalg.matrix_rank(B)
print("Rank:", rank)

if det != 0:
    inverse = np.linalg.inv(B)
    print("\nInverse of the Matrix:")
    print(inverse)
else:
    print("\nInverse does not exist")