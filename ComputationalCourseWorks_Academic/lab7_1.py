import numpy as np
from matplotlib import pyplot as plt

def fx(x):
	return x**3+4*x

def dfdx(x):
	return 3*(x**2)+4

a=0
b=0.8

s=[]
g=[]
deltax=[0.0,0.2,0.4,0.6,0.8]

for x in range (len(deltax)):
	xv =a+n*deltax[x]
	k=fx(x)*deltax[x]
	s.append(k)
	m=dfdx(x)*deltax[x]
	g.append(m)


print(s)
print(g)
plt.plot(s,g)
plt.show()












