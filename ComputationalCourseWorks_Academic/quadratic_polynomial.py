import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,50)
print(x)

def fx(x):
	return x**2-5*x+6

plt.plot(x,fx(x))
plt.xlabel("x")
plt.ylabel("y")
plt.axvline(0)
plt.axhline(0)
plt.title("x^2-5x+6")
plt.grid()
plt.show()
