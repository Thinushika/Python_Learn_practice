#this program is to plot polynomils
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10,10,100)
fx = []

for i in range(len(x)):
	fx.append((x[i]-4)*(x[i]+1)*(x[i]-2)*(x[i]-5)*(x[i]-7)*(x[i]+6)*(x[i]+8))

plt.plot(x,fx,'g')
plt.axvline(0)
plt.axhline(0)
plt.grid()
plt.show()