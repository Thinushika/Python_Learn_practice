
(base) C:\Users\PC>python
Python 3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np;
>>> import matplotlib as plt;
>>> A=np.array([[1,-1],[1,2]])
>>> A
array([[ 1, -1],
       [ 1,  2]])
>>> b= np.array([[2],[7]])
>>> A_inv=np.linalg.inv(A)
>>> A_inv
array([[ 0.66666667,  0.33333333],
       [-0.33333333,  0.33333333]])
>>> X=np.matmul(A_inv,b)
>>> X
array([[3.66666667],
       [1.66666667]])
>>>