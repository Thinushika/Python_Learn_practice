import numpy as np 
def mat_view(A):
	print(A)


A=np.array([[2,4,1],[3,-4,2]])
mat_view(A)


def sim_sol(A,b):
	A_inv=np.linalg.inv(A)
	X=np.matmul(A_inv,b)
	return X


A = np.array([[1,2,3],[-3,5,-2],[4,-2,1]])
b= np.array([[2],[-5],[7]])

print(is_invertible(A))
print(sim_sol(A,b))