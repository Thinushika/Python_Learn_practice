# Excercise 13 -- Parameters, Unpacking, Variables
from sys import argv
script, first, second, third = argv
## given arguments in the command line will assign to argv
print("The script is called : ",script)
print("Your first variable is :", first)
print("Your second variable is :", second)
print("Your third variable is :", third)

## when run this,
# need to give another Parameters,
####  EX:
###   python ex13.py first 2nd 3rd
###   python ex13.py stuff things that
