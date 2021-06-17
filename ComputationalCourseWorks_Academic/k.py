import numpy as np
print ("How to print a metrix")
a=np.array([[1,2,3],[5,4,6],[7,8,9]])
print(a)

print ("----------------------------------------------------------------------")
print("Transpose of a metrix")
mat=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(mat)
T_mat=np.transpose(mat)
#print("Transpose of metrix = ")
#print(T_mat)

print ("----------------------------------------------------------------------")
#Input :mat[][] = {{1, 2, 3},
  #                {6, 4, 5},
 #                 {2, 1, 3}};
#Output : Normal = 10  
 #        Trace = 8
#Explanation : 
#Normal = sqrt(1*1 +2*2 + 3*3 + 6*6 + 4*4 + 
 #            5*5 + 2*2 + 1*1 + 3*3)   
#Trace = 8(1+4+3)
# trace of matrix
import math

print ("Trace of matrix ")
mat=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(mat)


def find_trace(mat,n):
	sum=0
	for i in range(n):
		sum += mat[i][i]
	return sum

	
print ("Trace of matrix = ",find_trace(mat,4))


print ("----------------------------------------------------------------------")
print("Determinant of a metrix first method")
mat=np.array([[6,1,1],[4,-2,5],[2,8,7]])
mat_a=np.linalg.det(a)
print(mat_a)

print("Determinant of a metrix")

#determinant of 2x2 matrix
def det2x2(m):
	return m[0][0]*m[1][1]-m[0][1]*m[1][0]

mat=np.array([[6,1,1],[4,-2,5],[2,8,7]])
print(mat)

#a=mat[0][0]
#b=mat[0][1]
#c=mat[0][2]
#or just
a,b,c=mat[0]

# extract sub metrix
efhi=[x[1:]for x in mat [1:]]

#x[::2] :- from col index 0 to index 2 with step of 2
dfgi=[x[::2]for x in mat [1:]]
degh=[x[0:2] for x in mat[1:]]

det =(a*det2x2(efhi)
	-b*det2x2(dfgi)
	+c*det2x2(degh))
print (f"Determinant of matrix is :{det}")


print ("----------------------------------------------------------------------")
print("multiply metrix")
x=np.array([[12,7,3],[4,5,6],[7,8,9]])
y=np.array([[5,8,1,2],[6,7,3,0],[4,5,9,1]])
result=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
#iterate through rows of x
for i in range (len(x)):
	#iterate through columns of y
	for j in range(len(y[0])):
		# iterate through row of y
		for k in range (len(y)):
			result[i][j]+=x[i][k]*y[k][j]

for r in result:
	print(r)

print ("----------------------------------------------------------------------")
print("metrix addition")
x=np.array([[12,7,3],[4,5,6],[7,8,9]])
y=np.array([[5,8,1],[6,7,3],[4,5,9]])
result=np.array([[0,0,0],[0,0,0],[0,0,0]])
# itarate through rows
for i in range(len(x)):
	# itarate through columns
	for j in range(len(x[0])):
		result[i][j]= x[i][j]+y[i][j]

for r in result:
	print(r)

print ("----------------------------------------------------------------------")
print("metrix substraction")
import cmath
x=np.array([[12,7,3],[4,5,6],[7,8,9]])
y=np.array([[5,8,1],[6,7,3],[4,5,9]])
result=np.array([[0,0,0],[0,0,0],[0,0,0]])
# itarate through rows
for i in range(len(x)):
	# itarate through columns
	for j in range(len(x[0])):
		result[i][j]= x[i][j]-y[i][j]

for r in result:
	print(r)

print ("----------------------------------------------------------------------")
print("quadretic function")	
from math import sqrt
from matplotlib import pyplot as plt
from scipy import optimize
def fx(a,b,c):
	d=(b**2)-(4*a*c)
	sol1=(-b-cmath.sqrt(d))/(2*a)
	sol2=(-b+cmath.sqrt(d))/(2*a)

	print("Roots are : ")
	return sol1,sol2

a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
print(fx(a,b,c))
print("---------------------------")

p=int(input("Enter positive linaspace: "))
q=int(input("Enter negative linaspace: "))
x= np.linspace(p,q,100)
def function(x):
	return a*x**2+b*b*x+c

sol=optimize.root(function,[p,q])
plt.plot(x,function(x),lw=1,color="red")
plt.plot(sol.x,function(sol.x),'d',ms=7,color="green")
plt.axvline(0)
plt.axhline(0)
plt.ylabel("Y",color="blue")
plt.xlabel("X",color="blue")
plt.legend(["Function","Roots,","X&Y axis"],fontsize=7)
plt.grid()
plt.show()

print ("----------------------------------------------------------------------")
print("bisection method")	
a=0
b=30
tol=abs(a-b)
n_steps=100
c_value=[]
def func(x):
	return x*x-1

for i in range(n_steps):
	c=(a+b)/2
	c_value.append(c)
	print("---------------------------")
	print ("Iteration : ",i)
	print("a=" ,a)
	print("b=" ,b)
	print("c=" ,c)
	print("Tolarance (a-b)= ", tol)

	if func(c)==0:
		print("root is = ",c)
		break

	if(func(c)*func(a)<0):
		b=c

	else:
		a=c

	tol=abs(a-b)

plt.plot(c_value)
plt.show()

print ("----------------------------------------------------------------------")
print("regula falsi method")
a=0
b=30
tol=abs(a-b)
n_steps=100
c_value=[]
def func(x):
	return x*x-1

for i in range(n_steps):
	c=b-(func(b)*(b-a))/(func(b)-func(a))
	print("---------------------------")
	print ("Iteration : ",i)
	print("a=" ,a)
	print("b=" ,b)
	print("c=" ,c)
	print("Tolarance (a-b)= ", tol)
	c_value.append(c)

	if func(c)==0:
		print("root is = ",c)
		break

	if(func(c)*func(a)<0):
		b=c

	else:
		a=c

	tol=abs(a-b)

from matplotlib import pyplot as plt

plt.plot(c_value)
plt.show()	



print ("----------------------------------------------------------------------")
#print("Newton rapson method")
#c_value=[]
#def derivativeFunction(x):
	#return x**3+3

#for i in range(n_steps):
#	c=x-((x**3+3)/3*x**2)
#	print("---------------------------")
#	print ("Iteration : ",i)
#	print("Tolarance = ", tol)
#	c_value.append(c)

#	x=c

#from matplotlib import pyplot as plt

#plt.plot(c_value)
#plt.show()	
	
