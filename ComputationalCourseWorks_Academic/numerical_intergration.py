import math

def f(x):
	return x**2

a=1
b=3
n=4


def fx(a,b,n):
	delx=(b-a)/n
	sum=0
	for i in range(n):
		sum=sum+f(a+i*delx)+f(a+i*delx+1)
		endsum=sum*(1/2)*delx

	return sum


print(fx(a,b,n))

