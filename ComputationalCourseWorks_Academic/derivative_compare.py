from matplotlib import pyplot as plt

def fx(x):
	return x**4+x**2

def dfdx(x):
	return 4*(x**3)+2*x

def numerical_diff(x,delx):
	return (fx(x+delx)-fx(x))/delx

dx = [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.09,0.08,0.07,0.06,0.05,0.04,
0.03,0.02,0.01]

defd = []
ndefd = []

for delx in dx:
	ndefd.append(numerical_diff(1,delx))
	defd.append(dfdx(1))

plt.plot(dx,defd,'r',label='Exact Differetiation')
plt.plot(dx,ndefd,'bo-',label='Numerical Differetiation')
plt.xlabel('Delta x')
plt.legend(loc='upper left')
plt.show()