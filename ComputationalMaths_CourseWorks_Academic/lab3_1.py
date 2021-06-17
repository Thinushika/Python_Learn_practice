import numpy as np

#define the array a
A = np.array([[1,-3,2,-1,5],[3,2,-7,2,-1],[-1,1,3,-5,12],[2,4,-12,6,1],[1,1,-1,-3,-11]])
print(A)

#define the array b
B = np.array([[11],[-7],[24],[17],[-13]])
print(B)

#solve the linear equation
P=np.linalg.solve(A,B)
print(P)