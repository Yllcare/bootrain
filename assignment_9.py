# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 1
from functions_assign_9 import prime
if __name__ != '__main__':
      raise SystemExit('You called the code however it can only be run as the main program')
      
inp= input("Enter a number to verify if it is prime :")
if prime(int(inp)):
    print(inp, " is a prime number")
elif not prime(int(inp)):
    print(inp, " is NOT a prime number")
else:
    print("input error")
    

# 2
from functions_assign_9 import unique_list

aaa = [1,2,2,3,3,4,4,7,8,1,2,5,2,2,1,7,4]
print(unique_list(aaa))

# 3
from datetime import date

today = date.today()
birth=input("enter your birtday as in YYYYMMDD format")
dt_birth = date(int(birth[:4]),int(birth[4:6]), int(birth[6:]))
yearsOld = (today-dt_birth).days//365.25
print("You are {:.0f} years old.".format(yearsOld))

# 4
from functions_assign_9 import factorial
no = int(input("Enter a number:"))
print("factorial of",no,"is",factorial(no))

# 5
from functions_assign_9 import perfect
print(perfect(1,10000))

# 6
from functions_assign_9 import pascal
pascRowInp = int(input("enter number of rows for pascal's triangle:"))
all=pascal(pascRowInp)
print("\nPascal's triangle for",pascRowInp,"rows\n")
for n in range(len(all)):
    print(" "*(len(all)-n),all[n])
    


