x = [0,2,4,6,8,10,12]
y = []

for val in x:
	y.append(val**2+2)

var = 5

for i in range(len(x)):
	if x[i]<var<x[i+1]:
		k = i

interpol = y[k] + (y[k+1]-y[k])*(var - x[k])/(x[k+1]-x[k])


print(x)
print(y)
print(interpol)