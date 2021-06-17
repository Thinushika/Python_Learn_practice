print ("Hello world")

x=2
if x==1:
	print("x is 1")
else:
	print("x is not 1 ")

print ("Good bye world")
print ("-----------------------")

mint=4
mfloat=4.0

print(mint)
print(mfloat)

mfloat=float(7)
print(mfloat)
print ("-----------------------")
one=1
two=2
three=one+two
print(three)

hello="Hello"
world="World"
helloworld=hello+" "+world
print(helloworld)
print ("-----------------------")
a,b=3,4
print(a,b)
one=1
two=2
hello="Hello"

print(one+two)
print ("-----------------------")

mystring="Hello"
myfloat=10.0
myint=20

if mystring=="Hello":
	print("String :%s" % mystring)
if isinstance(myfloat,float)and myfloat==10.0:
	print("Float : %f"% myfloat)
if isinstance(myint,int)and myint==20:
	print("Integer: %d"% myint)

print ("-----------------------")
mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])#print 1
print(mylist[1])#print 2
print(mylist[2])#print 3

#prints out 1,2,3
for x in mylist:
	print(x)
print ("-----------------------")

numbers=[]
strings=[]
names=["John","Eric","Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("Hello")
strings.append("world")

socond_name=[]


print(strings)
print("The names on the name list is %s" % names)
print("The second name on the name list is %s" % names[1])
print("The first name on the name list is %s" % names[0])
print("The thired name on the name list is %s" % names[2])
print ("-----------------------")



#opertors
numbers=1+2*3/4.0
print(numbers)
reminder=11%3
print(reminder)
squared=7**2
cubed=2**3
print(squared)
print(cubed)
helloworld="hello"+" "+"world"
print(helloworld)
print ("-----------------------")
lots_of_hellos="hello"*10
print(lots_of_hellos)
print ("-----------------------")
even_numbers=[2,4,6,8]
odd_numbers=[1,3,5,7]
all_numbers=odd_numbers+even_numbers
print(all_numbers)
print ("-----------------------")
print([1,2,3]*3)
print ("-----------------------")
print ("-----------------------")

x=object()
y=object()

x_list=[x]*10
y_list=[y]*12
big_list=x_list+y_list

print("x_list contains %d object"% len(x_list))
print("y_list contains %d object"% len(y_list))
print("big_list contains %d object"% len(big_list))

if x_list.count(x) == 10 and y_list.count(y) >= 10:
	print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) >= 10:
	print("Great!")

import numpy as np
a=np.array([[1,2,3],[5,4,6],[7,8,9]])
print(a)

