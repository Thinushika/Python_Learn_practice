def star(n):
    for i in range(0, n):
        for j in range(0,i+1):
            print("*", end="")
        print("\r")
            
    for i in range(n,0, -1):
        for j in range(0, i-1):
            print("*", end="")
            
        print("\r")
    

star(10)

def pattern(n):
	if (n<=10000) and (n>=1):
		for i in range(0, n):
			for j in range(0,i+1):
				print("*",end="")
				j=j+1
			i=i+1
			print("\r")

		for i in range(n, 0, -1):
			for j in range(0,i-1):
				print("*",end="")

			print("\r")

pattern(10)
n=int(input("Input number of rows: \r"))
a=[]

for i in range(n):
    a.append([])
    a[i].append(1)
    
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
        
for i in range(n):
    print("   "*(n-i),end=" ",sep="   ")
    
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep="   ")
    print()