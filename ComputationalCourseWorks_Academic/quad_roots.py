import numpy as np
from matplotlib import pyplot as plt

#find availability of roots of a quadratic polynomial by inbuilt python function
#f(x) = ax^2+bx+c

def cal_roots(a,b,c):
	check = b**2-4*a*c
	return check


print(cal_roots(1,5,6))