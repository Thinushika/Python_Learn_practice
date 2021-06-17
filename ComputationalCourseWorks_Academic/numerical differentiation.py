import numpy as np
import matplotlib.pyplot as plt

def fx(x):
	return x**2+2*x

#def dfdx(x):
#	return 2*x+2


def deravative(x,deltax):
	return (fx(x+deltax)-fx(x)/deltax)


x=1
deltax=0.01
print (deravative(x,deltax))
