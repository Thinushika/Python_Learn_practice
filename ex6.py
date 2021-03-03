# Excercise 6 -- String and text
print('\n')

types_of_people = 10
print(f"There are {types_of_people} types of people around the world")
print('\n')
#before the quote should be add f that indicate format
#variable that need to be show in string
        #should be in {}

#Try different way
binary = "binary"
do_not = "don't"
x = f"There are {types_of_people} types of people."
y = f"Those who know {binary} and those who {do_not}." #predefined variables inside {}
                                                       #sentences also assigned to x & y
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'") #phrase inside quote because {y} is in single quote.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)
