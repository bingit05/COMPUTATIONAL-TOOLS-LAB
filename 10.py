import numpy as np

class Matrix:

    def __init__(self,A,B):
        self.A = np.array(A)
        self.B = np.array(B)

    def addition(self):
        return self.A + self.B
    
    def substraction(self):

        return self.A - self.B
    
    def multiplication(self):

        return np.dot(self.A, self.B)
    
    def transpose_A(self):

        return self.A.T
    
    def transpose_B(self):

        return self.B.T
    

A = [[1,2],
    [3,4]]
    
B = [[5,6],
     [7,8]]
    

matrix = Matrix(A,B)


print("Matrix A")
print(matrix.A)

print("matrix B")
print(matrix.B)

print("\nAdditon")
print(matrix.addition())


print("\nsubs")
print(matrix.substraction())

print("\nmultiplication")
print(matrix.multiplication())

print("\ntranspose of A")
print(matrix.transpose_A())

print("\ntrans of B")
print(matrix.transpose_B())