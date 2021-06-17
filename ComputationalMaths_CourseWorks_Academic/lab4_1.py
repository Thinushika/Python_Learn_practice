#import numpy as np
import cmath
#from matplotlib import pyplot as plt
#from scipy import optimize

a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))

def fx(a,b,c):
	d=(b**2)-(4*a*c)
	sol1=(-b-cmath.sqrt(d))/(2*a)
	sol2=(-b+cmath.sqrt(d))/(2*a)

	
	return sol1,sol2
print("Roots are : ",fx(a,b,c))
print("---------------------------")