import numpy as np
import matplotlib as plt
A=np.array([[1,-1],[1,2]])
A

b= np.array([[2],[7]])
A_inv=np.linalg.inv(A)
A_inv

X=np.matmul(A_inv,b)
X
