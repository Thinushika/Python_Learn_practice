import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,50)
def f(x):
	return x**3+3*x**2-x+1

plt.plot(x,f(x))
plt.xlabel("x")
plt.ylabel("y")
plt.title("x^3+3x^2-x+1")
plt.grid()
plt.show()

