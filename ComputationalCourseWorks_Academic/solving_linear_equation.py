 #[[1,4,0],[3,8,3],[0,1,2]]
#[16,92,18]

import numpy as np
import matplotlib.pyplot as plt
a=np.array([[1,4,0],[3,8,3],[0,2,1]])
b=np.array([[16],[92],[18]])

# a convert to inverse
#a_inv=np.linalg.inv(a)
#print("A inverse : ",a_inv)

#1st way
#result=np.matmul(a_inv,b)
#print("result : ",result)

#2nd way 
print(np.linalg.solve(a,b))

#generate sequence of numbers 
x=np.linspace(-2,2,10)
#print(x)

fx=[]
for i in range (len(x)):
	fx.append(2*x[i]+3)

plt.plot(x,fx)
plt.xlabel("x")
plt.ylabel("y")
plt.title("function = 2x+3 ")
plt.grid()
plt.show()
