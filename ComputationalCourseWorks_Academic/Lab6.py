a=0
b=30
tol=abs(a-b)
n_steps=100
c_value=[]
def func(x):
	return x*x-1

for i in range(n_steps):
	c=(a+b)/2
	c_value.append(c)
	print("---------------------------")
	print ("Iteration : ",i)
	print("a=" ,a)
	print("b=" ,b)
	print("c=" ,c)
	print("Tolarance (a-b)= ", tol)

	if func(c)==0:
		print("root is = ",c)
		break

	if(func(c)*func(a)<0):
		b=c

	else:
		a=c

	tol=abs(a-b)

from matplotlib import pyplot as plt

plt.plot(c_value)
plt.show()
