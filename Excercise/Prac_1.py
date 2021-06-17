"""print("Hello, world")

x,y,z = "AAA", "BBB", "CCC"
print(x)
print(y)
print(z)

x=y=z = "Orange"
print(x)
print(y)
print(z)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

x = 1j
print(type(x))

import random
print(random.randrange(1,10))

x =int(1)
print(x)
print(type(x))

y =int(0.25)
print(y)
print(type(y))

z =int("34")
print(z)
print(type(z))

a =float("3")
print(a)
print(type(a))

b =str(3.25)
print(b)
print(type(b))

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

a = "Hello"
b = "World"
c = a + b
print(c)

age = str(36)
txt = "My name is John, I am " + age
print(txt)

age = 36
txt = "My name is John, I am {}"
print(txt.format(age))"""

"""class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))"""
"""def function():
	return True


print(function())"""

x = 'abc'
x = x[::-1]
print(x)

set = {9,1,-1,5,2,8,3, 8}
print(set)

var_one = 123
def func_one(var_one):
    var_one = 234
    var_three = 'abc'
var_two = 456
print(dir())