import numpy as np
from matplotlib import pyplot as plt
def fx(x):
	return x**3+4*x

def dfdx(x):
	return 3*(x**2)+4
 

x0=0.2
h_vec=[0.2,0.3,0.4,0.5,0.6,0.7,0.8]
for i in range(x,h_vec):
	sol=(f(x+h_vec)-f(x))/(h_vec)


plt.figure(dpi=100)
plt.loglog(label="Numerical differntiation")
plt.grid()
plt.xlabel("h")
plt.ylabel("Exact differntiation")
plt.legend()
plt.show()