import numpy as np
from matplotlib import pyplot as plt
# matrix A
A = np.array([[1,-3,2,-1,5],[3,2,-7,2,-1],[-1,1,3,-5,12],[2,4,-12,6,1],[1,1,-1,-3,-11]])
print(A)
# matrix B
B = np.array([[11],[-7],[24],[17],[-13]])
print(B)

# convert A to A_inv
A_inv = np.linalg.inv(A)
print(A_inv)

# multiply A_inv by B
X = np.matmul(A_inv,B)
print(X)

# # multiply A by B
P=np.linalg.solve(A,B)
print(P)

x = np.linspace(-10, 10, 50)# parameterers of x axis
def f(x): # funtion to find Y values
    return x**4 - 3*x**3 + -35*x**2 + 39*x + 70


print("roots = ",np.roots([1, -3, -35, 39, 70]))
 
plt.plot(x,f(x))
plt.grid()
plt.axvline(0)
plt.axhline(0)
plt.show()