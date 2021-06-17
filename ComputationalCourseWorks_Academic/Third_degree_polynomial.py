import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,50)
print(x)

def fx(x):
	return 3*x**3-4*x+7

plt.plot(x,fx(x))
plt.xlabel("x")
plt.ylabel("y")
plt.title("3x^3-4x+7")
plt.grid()
plt.show()