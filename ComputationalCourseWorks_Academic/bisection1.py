def f(x):
	f = x**3+4*x**2-10
	return f

print ("Sample input : bisectionMethod (12,10**-4,100)")

def bisectionMethod(a,b,TOL,N):
	i = 1
	FA = f(a)

     
      
    while(i <= N):
        p = a + (b-a)/2
        FP = f(p)
          
        if(FP == 0 or (b-a)/2 < TOL):
            break
        else:
             print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (i, a, b, p, f(p)))
         
          
        i = i + 1
          
        if(FA*FP > 0):
            a = p
        else:
            b = p
      
    return