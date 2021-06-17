import numpy as np
from matplotlib import pyplot as plt


x = np.linspace(-10, 10, 50)
def function(x):
    return -x**5-2*x**4+(-x**3)-4*x**2+8*x+30


 
plt.plot(x,function(x))
plt.grid()
plt.axvline(0)
plt.axhline(0)
plt.show()
