print(2<3)
print(3<2)
x=5
print(2<x<10)
print(2<3<4<5<6)

print("python">"perl")
print("python" > "java")
print(True and True)
print(True and False)
print(2<3 and 5<4)
print(2<3 and 4<5)
print(2<3 and 3>1)
print(2<3 or 3>1)
print(2<3 or not 3>1)
print(2<3 and not 3>1)
x=4
y=5
p= x<y or x<z
print(p)

print("if without else")
x=42
if x % 2 ==0:print('even')

print("if with else")
x=3
if x % 2 == 0:
	print("even")
else:
	print('odd')

print("if with elif")
x=42
if x<10:
	print('one digit number')
elif x<100:
	print('two digit number')
else:
	print('big number')




