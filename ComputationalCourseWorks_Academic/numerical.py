import numpy as np
from matplotlib import pyplot as plt


x = np.linspace(-10, 10, 50)
def function(x):
    return x**4 - 3*x**3 + -35*x**2 + 39*x + 70
 
plt.plot(x,function(x))
plt.grid()
plt.axvline(0)
plt.axhline(0)
plt.show()





