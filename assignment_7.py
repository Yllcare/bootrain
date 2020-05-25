#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 00:56:50 2020

@author: illcare
"""

# 1
degree = input("please enter the temparature (as in 30C or 40F) :")
unit = degree[-1]
degree = int(degree[:-1])
if unit=="F":
    C = (5/9) * (degree - 32)
    print(degree,"fahrenheit is", C, "celcius")
elif unit=="C":
    F = (9/5)*C+32
    print(degree, "celcius is", C,"fahrenheit")
else:
    print("something went wrong with the input")# one of many that can go wrong with the input
    
    
# 2. what does this have anything to do with conditionals?
# "Please form a list out of Fibonacci numbers from 1 to 50. The first two Fibonacci numbers are 1. 
# The next numbers are the sum of the previous two."

# 3
serv = input("please enter total years of service :")
if int(serv)>5:
    sal = input("please enter your salary :")
    bonus= int(sal)*0.05
    print("your bonus payment is", bonus, "usd")
else:
    print("no bonus for you")
    
    

# 4 : i could do this by converting into list and sortin but the goal seems studying conditionals
x, y, z = input("Enter ages of three people seperated by space: ").split() 
x, y, z = int(x), int(y), int(z)
if x>y:
    if x>z:
        print(x,"is largest")
        if y>z:
            print(z,"is smallest")
        else:
            print(y,"is smallest")
    elif x<z:
        print(z,"is largest")
        print(y,"is smallest")
elif x>z:
    print(y,"is largest")
    print(z,"is smallest")
else:
    if y>z:
        print(y,"is largest")
    else:
        print(z,"is largest")
    print(x,"is smallest")
    
    

# 5
x,y = input("please enter classes held and attended seperated by space:").split()
held, att = int(x),int(y)
if att>held:
    print("you entered values wrong dude")
else:
    thresh=held*0.75
    perc=(att/held)*100
    print("attendance percentage is {:.1f} %".format(perc))
    if thresh>att:
        print("you can NOT take the exam")
    else:
        print("you can take the exam")
        
        

# 6
lett=input("please enter a letter:")
if lett=="a" or lett=="e" or lett=="i" or lett=="o" or lett=="u":
    print(lett,"is a wovel")
elif lett=="y":
    print("y is sometimes read as a wovel and sometimes as a consonant")
else:
    print(lett, "is a consonant")
