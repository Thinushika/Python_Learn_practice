import numpy as np
A = np.array([[1,2,3],[4,5,6]])
print(A)
print(np.transpose(A))
B = np.transpose(A)
print(B)

C = np.array([[1,2],[4,5]])
print(C)
D = np.array([[1,2,3],[4,5,6]])
print(D)
X = np.linalg.dot(C,D)
print(X)