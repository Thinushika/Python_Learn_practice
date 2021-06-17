import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize


x= np.linspace(10,-10,100)
def function(x):
	return 2*x**2+2*x-5

#sol=optimize.root(function,[x])
plt.plot(x,function(x),lw=1,color="red")
#plt.plot(sol.x,function(sol.x),'d',ms=7,color="green")
plt.axvline(0)
plt.axhline(0)
plt.ylabel("Y",color="blue")
plt.xlabel("X",color="blue")
plt.legend(["Function","X&Y axis"],fontsize=7)
plt.grid()
plt.show()