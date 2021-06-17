import numpy as np
print("Question 1 : ")
a=np.array([45,35,60])
print(a)
print("")

b=np.array([2,2,2])
print("Question 2 : ")
print(a+b)
print("")


print("Question 3 : ")
c=np.array([[3,12,7,11],[4,0,8,5],[5,4,14,9],[1,-2,3,3]])
d=np.array([[2,3,4,5],[11,2,33,4],[3,3,3,3],[2,2,2,2]])
print("Sum = ",c+d)
print("")

print("product of a*b = ",c*d)
print("")

print("product of b*a =",d*c)
print("")

print("shape = ",c.shape)

print("")
print("Question 4 : ")
print(np.linalg.det(c))

print("")
print("Question 5 : ")
print(np.trace(c))