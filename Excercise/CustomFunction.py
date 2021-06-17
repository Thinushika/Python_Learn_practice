def Square(x):
	return x*x


print(Square(5))
print(Square(2)+Square(3))
print(Square(Square(3)))




#Existing functions using in creating new functions
f=Square
print(f(4))

def fxy(f,x,y):
	return f(x)+f(y)

print(fxy(Square,2,3))

#=============================================
x=0
y=0
def incr(x):
     y=x+1
     return y

incr(5)
print (x,y)
#=============================================
print("problem 1")
pi = 3.14
def area(r):
	return pi * r * r

print (area(5))
#=============================================
print("problem 2")
numcalls = 0
def square(x):
	global numcalls
	numcalls = numcalls+1
	return x * x

print (square(5))
print (square(2*5))

#=============================================
print("problem 3")
x = 1
def f():
    return x
print (x)
print (f())

#=============================================
print("problem 4")
x=1
def f():
	x=2
	return x

print(x)
print(f())
print(x)
#===============================================
print("problem 5")
x = 1
def f():
    
    x = 2
    y = x
    return x + y

print (x)
print (f())
print (x)


#===============================================
print("problem 6")

x=2
def f(a):
	x=a*a
	return x

y=f(3)
print (x,y)

#===============================================
print("functions from keyword arguments")

def defference(x,y):
	return x-y

print(defference(5,2))
print(defference(x=5,y=2))
print(defference(5,y=2))
print(defference(y=2,x=5))


#===============================================
print("arguments can have default values")
def increment(x,amount=1):
	return x+amount

print(increment(10))
print(increment(10,5))
print(increment(10,amount=2))

#===============================================
print("creating function using lambda operator")

cube = lambda x:x**3
print(fxy(cube,2,3))
print(fxy(lambda x:x**3,2,3))

#===============================================
print("python built in functions")
print(min(2,3,4,5,1))
print(max(5,3,7,1,9))


print(len("helloworld"))
print(int("50"))
print(str(123))

#===============================================
print("python methods")
x="hello"
print(x.upper())

f=x.upper
print(f())

#===============================================
#print("function istrcmp to compare two strings, ignoring the case")
#print(istrcmp('python','python'))
#print(istrcmp('LaTex','Latex'))
#print(istrcmp('a','b'))

#===============================================
