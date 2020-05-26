#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 02:08:32 2020

@author: illcare
"""

# 1
num = input("enter a number :")
while not num.isdigit():
    print("\n")
    num=input("Enter a NUMBER! : ")
    
for n in range(1,11):
    print(n,"x", num,"=", n*int(num))
    
# 2
theList = []
for num in range(1,21):
    if num%2==1:
        theList.append(num**2)
    else:
        theList.append(num**3)
        
print(theList)

# 3
word=input("enter a word or number:")
for n in range(len(word),0,-1):
    print(word[n-1],end='')
    
# 4
odds,evens = [],[]
for num in range(1,201):
    if num%2==1:
        odds.append(num)
    else:
        evens.append(num)
        
# 5
sequence = [1, 2, 3, 1, 5, 4, 8, 9, 8, 5, 5, 6]
item = 1
count = 0
for n in sequence:
    if n==item:
        count += 1
        
# 6
numbers = input("enter a high number :")
while len(numbers)>1:
    sum=0
    for n in numbers:
        sum += int(n)
        
    print(sum)
    numbers = str(sum)
    
# 7
x, y = input("enter 2 numbers seperated by space :").split() #OBEB
lst=[int(x),int(y)]
lst.sort()
x=lst[0]
y=lst[1]
if y%x==0:
    print("GCD is",x)
else:
    for n in range(x//2,0,-1):
        if y%n==0 and x%n==0:
            print("GCD is", n)
            break
        
# 8
for n in range(1,51):
    if n%15==0:
        print("fizzBuzz")
    elif n%3==0:
        print("fizz")
    elif n%5==0:
        print("buzz")
    else:
        print(n)
        
