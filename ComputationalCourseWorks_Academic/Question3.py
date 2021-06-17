import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

x=np.linspace(-10,10,100)
print(x)
def fun(x,a=1, b=3, c=35, d=39, e=70):
    return a*x**4 -b*x**3 -c*x**2 +d*x +e
 
sol = optimize.root(fun,[-7, 1, 3, 7.5])
plt.plot(x,fun(x))
plt.plot(sol.x,fun(sol.x),'d',ms=10)
plt.grid()
plt.axvline(0)
plt.axhline(0)
plt.show()
