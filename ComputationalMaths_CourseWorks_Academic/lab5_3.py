def func(x):
	a=1
	b=-3
	c=-4
	return a*x*x+b*x+c

x=-5
k=0
while k!=1:
	fx = func(x)
	if fx == 0:
		k=1
		break

	x=x+1

while k!=1:
	fx = func(x)
	if fx == 0:
		k=1
		break

	x=x+1

print("root = ",x)

	