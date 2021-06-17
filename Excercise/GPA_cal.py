import numpy as np
# assin subject grade and point
#"A+" =4.0
#"A"  =4.0
#"A-" =3.7
#"B+" =3.3
#"B"  =3.0
#"B-" =2.7
#"C+" =2.3
#"C"  =2.0
#"C-" =1.7
#"D+" =1.3
#"D"  =1.0
#"E"  =0.0

#get user input
n=int(input("Enter number of subjects: "))

#get user input for grade and subject credit
credit_sum = 0
point_sum =0.0
gpa_val =0

for i in range(n):
	Grade=float(input("Enter your grade point: "))
	Cradict=float(input("Enter subject cradict: "))
	
	credit_sum = credit_sum+Cradict
	 
	point_sum =point_sum+(Grade*Cradict)

	gpa_val = point_sum/credit_sum


print ("your GPA = ",gpa_val)

#--------------------------------------------------------------------------------

		

		
		