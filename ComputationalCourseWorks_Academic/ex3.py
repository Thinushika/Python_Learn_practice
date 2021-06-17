import numpy as np
import matplotlib.pyplot as plt
A = np.array([[1,-3,2,-1,5],[3,2,-7,2,-1],[-1,1,3,-5,12],[2,4,-12,6,1],[1,1,-1,-3,-11]])
print(A)
B = np.array([[11],[-7],[24],[17],[-13]])
print(B)
A_inv = np.linalg.inv(A)
print(A_inv)
X = np.matmul(A_inv,B)
print(X)

P=np.linalg.solve(A,B)
print(P)

X = np.linspace(-2,2,num=10)
print(X)

fx=[]
for i in range(len(X)):
    fx.append(2*X[i]+3)
    
print(fx)
plt.plot(X,fx)
plt.show()

plt.plot(X,fx)
plt.grid()
plt.axvline(0)
plt.axhline(0)
plt.show()