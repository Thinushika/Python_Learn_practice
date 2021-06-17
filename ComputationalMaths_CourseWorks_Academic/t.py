import cmath
#from matplotlib import pyplot as plt
#from scipy import optimize

a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))

d=b**2-4*a*c


if d<0:
	print("this has no real solution")
elif d==0:
	sol1=(-b-cmath.sqrt(d))/(2*a)
	print("this has one solution",sol1)
else:
	sol1=(-b-cmath.sqrt(d))/(2*a)
	sol2=(-b+cmath.sqrt(d))/(2*a)
	print("this has two solution",sol1 ,"or",spl2) 


#print("Roots are : ",fx(a,b,c))
print("---------------------------")