import numpy as np
from matplotlib import pyplot as plt

#enter an array into python
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)
print(A[1,1])
print(np.trace(A))
print(A.shape)
print(np.linalg.det(A))