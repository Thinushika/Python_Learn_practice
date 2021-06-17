import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 50)

def f(x):
    return x**2-x-2

plt.plot(x,f(x))
plt.grid()
plt.axvline(0)
plt.axhline(0)
plt.show()