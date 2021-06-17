#Define function to integrate
def fx(x):
	return x**2

#Define the exact integration
def intfx(x):
	return (x**3)/3

#Integral limits
a = 1
b = 3
# 'n' is number of divisions
n = 4
deltax = (b-a)/n
#initialize sum to zero
sum = 0.0

for i in range(n):
	xval = a+i*deltax
	sum = sum + fx(xval)*deltax

print(intfx(b)-intfx(a))
print(sum)
