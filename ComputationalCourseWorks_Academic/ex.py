import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

#x=np.linspace(-100,100,1000)
#rint(x)
#def fun(x,a=99):
 #   return x**2 -a*x -100
 

#print(np.roots([1, -99, -100]))
#plt.plot(x,fun(x))
#plt.grid()
#plt.axvline(0)
#plt.axhline(0)
#plt.show()

x=np.linspace(-10,10,100)
print(x)
def fun(x):
    return x**3 -x -11
 

print(np.roots([1, -1, -11]))
plt.plot(x,fun(x))
plt.grid()
plt.axvline(0)
plt.axhline(0)
plt.show()
