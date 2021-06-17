import math

def f(x):
	return math.sin(x)+math.tan(x)

a=3
b=5
n=1000


delx=(b-a)/n
sum=0
endsum=0
for i in range(n):
	sum=sum+f(a+(i*delx))+f(a+((i+1)*delx))
	endsum=(sum*delx)/2

print(endsum)

