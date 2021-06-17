def f(x):
	return x**2

a=2
b=6
n=4
def fx(a,b,n):
	delx=(b-a)/n
	sum=0
	endsum=0
	for i in range(n):
		sum=sum+(f(a+i*delx)+f(a+(i+1)*delx))*0.5*delx
		#print((sum*delx)/2)

	return sum


print(fx(a,b,n))
