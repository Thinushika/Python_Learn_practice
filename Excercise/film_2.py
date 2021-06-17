
s = int(input("Enter number of sinhala film do you want : "))
h = int(input("Enter number of hindi film do you want : "))
e = int(input("Enter number of english film do you want : "))
t = int(input("Enter number of tamil film do you want : "))

price = ((s*200)+(h*300)+(e*800)+(t*400))

print("Your bill price is : ",price) 


import numpy as np

print("\n[1] Enter S for Sinhala film.")
print("\n[2] Enter E for English film.")
print("\n[3] Enter H for Hindi film.")
print("\n[4] Enter T for Tamil film.")

count=0
price=0
total_price=0
answer='Y'

while count<5:	
    ftype = input("Enter film type: ")
    print(ftype)
    
    if ftype=="S":
        price = 200
    elif ftype=="H":
        price = 300
        print("AAA")
    else:
        print("it is invalid")
        print("Your total price is : ",total_price)
        
    answer = input("Do you want to add more film types : (Y/N)" )
    if answer!='Y':
        break
        
                        
    total_price=total_price+price
    print(total_price)
    count += 1

