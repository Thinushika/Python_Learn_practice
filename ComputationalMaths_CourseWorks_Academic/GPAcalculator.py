import numpy as np

n=int(input("Enter number of subjects: "))

#G=np.array([4.0,4.0,3.7,3.3,3.0,2.7,2.3,2.0,1.7,1.3,1.0,0.0])
#C=np.array(["A+","A","A-","B+","B","B-","C+","C","C-","D+","D","E"])




nval=0
xval=0.0
for i in range(n):
	Grade=float(input("Enter your grade: "))
	Cradict=float(input("Enter subject cradict: "))
	for i in range (n):
		xval=xval+Grade
		nval=nval+Cradict
	
	
	gpa=(xval/nval)

print ("your GPA = ",gpa)