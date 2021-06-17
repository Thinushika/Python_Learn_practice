#import numpy as np
#import matplotlib.pyplot as plt

a=2
b=5
tol=abs((a-b))
n_steps=100
#c_value=[]

def function(x):
	return x-3

for i in range(n_steps):
	c=(a+b)/2
	#c_value.append(c)
	print("------------------------------------------")
	print("iteration :",i)
	print("a = ",a)
	print("b = ",b)
	print("c = ",c)
	print("Tolarance (a-b) = ",tol)

	if function(c)==0:
		print("root is = ",c)
		break
	if (function(c)*function(a)<0):
		b=c
	else:
		a=c
	tol=abs(a-b)

#plt.plot(c_value)
#plt.grid()
#plt.show()