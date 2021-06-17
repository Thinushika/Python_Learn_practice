import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))

p=int(input("Enter positive linaspace: "))
q=int(input("Enter negative linaspace: "))


x= np.linspace(p,q,100)
def function(x):
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