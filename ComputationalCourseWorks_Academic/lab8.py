import math

def f(x):
	return sin(x)

def num_def(x,deltax):
	return (f(x+deltax)-f(x))/deltax

x=1
deltax=0.0001
print (num_def(x,deltax))