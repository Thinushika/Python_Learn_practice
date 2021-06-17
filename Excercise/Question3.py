import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

X=np.linspace(-10,10,100)
def f(x):
    return x**4 - 3*x**3 + -35*x**2 + 39*x + 70
 
solution = optimize.root(fun,[-7, 1, 3, 7.5])
plt.plot(x,fun(x),lw=3)
plt.plot(solution.x,fun(solution.x),'39',ms=10)
plt.grid()
plt.axvline(0)
plt.axhline(0)
plt.show()
