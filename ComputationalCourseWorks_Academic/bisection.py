#define starting values 'a' and 'b'
a=0
b=30
#tolerance value 
tol=abs(a-b)
#number of steps
n_steps = 100

#define the function separately
def func(x):
	return x*x-1

#for loop for the calculation of the root
for i in range(n_steps):
	c = (a+b)/2
	print('------------------------------')
	print('Iteration :',i)
	print('a=',a)
	print('b=',b)
	print('c=',c)
	print('Tolerance (a-b) = ',tol)

	#stop if the function converged to a solution
	if func(c)==0:
		print('root is = ',c)
		break

	#deciding 'a' and 'b' values for the next iteration
	if (func(c)*func(a)<0):
		b=c

	else:
		a=c
	#calculate tolerance value	
	tol=abs(a-b)