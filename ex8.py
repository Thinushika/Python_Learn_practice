#printing printing
formatter = "{} {} {} {}" #this function just like the command line command
                            #that tell what to do

print(formatter.format(1,2,3,4)) #print numbers using funtion
print(formatter.format("one","two","three","four")) #string printing
print(formatter.format(True, False, False,True)) #boolean printing
print(formatter.format(formatter,formatter,formatter,formatter)) #just printing
print(formatter.format("Try your",
                        "Own text here",
                        "Maybe a poem",
                        "Or a song about fear")) #same trick(print string)
