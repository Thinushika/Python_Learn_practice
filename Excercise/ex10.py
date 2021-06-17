#
# \ character encodes difficult to type characters into string
# we can use single and double quotes to escape characters

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslahs_cat = "I'm \\ a \\ cat"

#multiline string writing
#\t for tab space
#\n for new line
fat_cat = """
I'll do a list:
\t*Cat Food
\t*Fishes
\t*Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslahs_cat)
print(fat_cat)
print('\n')
