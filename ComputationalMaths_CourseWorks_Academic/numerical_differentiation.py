import math

def f(x):
	return math.sin(x)

#def dfdx(x):
#	return 2*x+2


def deravative(x,deltax):
	return (f(x+deltax)-f(x))/deltax


x=1
deltax=0.0001
print (deravative(x,deltax))
