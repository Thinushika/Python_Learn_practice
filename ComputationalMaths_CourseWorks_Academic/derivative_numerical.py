import math
#define your function here
def f(x):
	return math.sin(x)

#calculate the numerical derivative of the function
def num_def(x,delx):
	return (f(x+delx) - f(x))/delx


x = 1
deltax = 0.01
#print the numerical derivative 
print(num_def(x,deltax))