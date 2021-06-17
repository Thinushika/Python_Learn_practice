import numpy as np
from matplotlib import pyplot as plt


a=1
b=4
tol=abs(a-b)

def func(x):
	return x*x-2*x


for i in range(4):
	
	c = b - func(b)*(b-a)/(func(b)-func(a))
	print('------------------------------')
	print('step :',i)
	print('a=',a)
	print('f(a)',func(a))
	print('b=',b)
	print('f(b)',func(b))
	print('c=',c)
	print('f(c)',func(c))
	print('Tolerance (a-b) = ',tol)

	if func(c)==0:
		break

	if (func(c)*func(a)<0):
		b=c
	else:
		a=c
	tol=abs(a-b)
	
