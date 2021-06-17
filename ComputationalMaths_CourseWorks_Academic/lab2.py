import numpy as np
#Question number 3
friends=[]
i=0
print("Enter 5 of your friends names : ")
while i<5:
	friends.append(input())
	i+=1

print(friends)


#Question number 2
A=np.array([[1,2,3],[4,5,3],[7,8,9]])
B=np.array([[7,6,9],[4,4,6],[1,1,3]])
for i in range(3):
	x=A[i]+B[i]
	print(x)

#Question number 3
i=0
j=0
for i in range(10):
	for j in range(10):
		j+=j
	print("*"*i)	
	i+=i