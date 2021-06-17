a=1
b=-2
tol=abs(a-b)
n_steps=10
c_value=[]
def func(x):
	return x**3-1

for i in range(n_steps):
	c=b-(func(b)*(b-a))/(func(b)-func(a))
	print("---------------------------")
	print ("Iteration : ",i)
	print("a=" ,a)
	print("b=" ,b)
	print("c=" ,c)
	print("Tolarance (a-b)= ", tol)
	c_value.append(c)

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



#------------------------------------------------------
def fx(x):
	return x**2+4

def intfx(x):
	return(x**3)/3+4*x


a=2
b=3
n=10
deltax=(b-a)/n
sum=0.0

for i in range(n):
	c=a+i*deltax
	sum=sum+fx(c)*deltax
	

print (intfx(b)-intfx(a))
print(sum)