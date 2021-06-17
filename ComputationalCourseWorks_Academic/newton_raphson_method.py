#import numpy as np
#import matplotlib.pyplot as plt

def fun1(x):
	return 3*x**2+2

def fun2(x):
	return 2*x
x=1
#i=1
n_steps=4
#c_value=[]

#x=np.linspace(-10,10,50)

for i in range (n_steps):
	c=x-((x**2-17)/(2*x))
	x=c
	#c_value.append(c)
	print("iteration : ",i)
	print("c : ",c)
	print("-----------------------")


#plt.plot(c_value)
#plt.grid()
#plt.show()
