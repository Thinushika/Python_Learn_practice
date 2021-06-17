import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

x= np.linspace(p,q,100)
def function(fx):
	#enter function here
	return a*x**2+b*x+c

sol=optimize.root(function,[p,q])
plt.plot(x,function(x),lw=1,color="red")
plt.plot(sol.x,function(sol.x),'d',ms=7,color="green")
plt.axvline(0)
plt.axhline(0)
plt.ylabel("Y",color="blue")
plt.xlabel("X",color="blue")
plt.legend(["Function","Roots,","X&Y axis"],fontsize=7)
plt.grid()
plt.show()
