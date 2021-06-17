def f(x):
	return x**2+2*x
#numerical approximation
def dfdx(x,deltax):
	return (f(x**2+deltax)-f(x))/deltax

x=1
deltax=0.01
print(dfdx(x,deltax))

