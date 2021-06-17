import numpy as np
import matplotlib as plt
A = np.array([[1,-3,2,-1,5],[3,2,-7,2,-1],[-1,1,3,-5,12],[2,4,-12,6,1],[1,1,-1,-3,-11]])
A
B = np.array([[11],[-7],[24],[17],[-13]])
B
A_inv = np.linalg.inv(A)
A_inv
X = np.matmul(A_inv,B)
X
np.linalg.solve(A,B)
X = np.linspace(-2,2,num=10)
X