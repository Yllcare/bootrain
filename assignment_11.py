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
        return res
    except ZeroDivisionError:
        print("Divisor can not be zero")
    except NameError:
        print("Global or not, whatever name is absent error")
        
d = div(20,0)
print(d)

# 2
def sqr(no):
    try:
        n = int(no)
        return n**2
    except ValueError:
        print("enter a valid value, meaning a number")
        

nono = input("insert a number :")
print("square of the number you entered is", sqr(nono))