import numpy as np
import math
a=np.array([[4,0,5],[2,3,4]])
b=np.array([[4,0,1],[3,4,4]])
x=a*b
#r=np.dot(a,b)
#o=np.matmul(a,b)
p=np.array([[1,4,0],[3,8,3],[0,2,1]])
q=np.array([[16],[92],[18]])
n=p*q
y=np.matmul(p,q)
print(x)
#print(o)
print(y)
print(n)

print("-----------------------------")
p=np.array([[1,2,0,1],[0,2,3,0],[0,1,1,0],[1,0,-1,0]])
w=np.linalg.det(p)
print(w)