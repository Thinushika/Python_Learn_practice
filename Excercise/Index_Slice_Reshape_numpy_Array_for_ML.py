# from list to array
## one dimentional list to array

### one dimentional example
from numpy import array



print("One dimentional array example:")
#list of data
data = [11, 22, 33, 44, 55]
# array of data
data = array(data)
print(data)
print(type(data))


print("")


### two dimentional example
print("Two dimentional array example:")
data = [[11, 22],
		[33, 44],
		[55, 66]]
# array of data
data = array(data)
print(data)
print(type(data))


print("")

#array indexing
#one dimentional indexing
print("one dimentional indexing:")
# define array
data = array([11, 22, 33, 44, 55])
# index data
print(data[0])
print(data[4])
# define array
data = array([11, 22, 33, 44, 55])
# index data
print(data[-1])
print(data[-5])


print("")

# 2d indexing
# define array
data = array([[11, 22], [33, 44], [55, 66]])
# index data
print(data[0,0])
print(data[0,])
print(data[1,1])

# simple slicing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data[:])


# simple slicing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data[0:1])


# simple slicing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data[-2:])



