#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 01:26:06 2020

@author: illcare
"""
# 1
def div(dvdnd,dvsr):
    try:
        res = dvdnd/dvsr
        print("\ndivision result is : ",res,sep="")
        return res
    except ZeroDivisionError:
        print("\nDivisor can not be zero")
        
d = div(20,0)

# 2
def div(dvdnd,dvsr):
    try:
        res = dvdnd/dvsr
        prit("\ndivision result is : ",res,sep="")
        return res
    except NameError:
        print("\nGlobal or not, whatever. It is a nameError")
        
d = div(20,2)

# 3
def sqr(no):
    try:
        n = int(no)
        print("square of the number you entered is", n**2)
        return n**2
    except ValueError:
        print("enter a valid value, meaning a number")
        

nono = input("insert a number :")
result = sqr(nono)