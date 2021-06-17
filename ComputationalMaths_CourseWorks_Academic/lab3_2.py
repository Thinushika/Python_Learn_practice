import numpy as np
from matplotlib import pyplot as plt

c=[]
#give x parameters and no.of divitions
x = np.linspace(-10, 10, 50)

#difine the given function
def f(x):
    return x**4 - 3*x**3 + -35*x**2 + 39*x + 70

#plot the function 
plt.plot(x,f(x))#call x parameters and f(x) function to give y values
plt.grid()
plt.axvline(0)#draw x axis
plt.axhline(0)#draw y axis
plt.show()

print(max.f(x))
print(np.roots([1, -3, -35, 39, 70]))# to find the roots, give values on the function with signs(-/+)