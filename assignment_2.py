#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:22:59 2020

@author: illcare
"""
# bitcoin gain calculation
capital = 1000
days = 7
incAndCap = 1.12
finalCap = (((((((capital*incAndCap)*incAndCap)*incAndCap)*incAndCap)*incAndCap)*incAndCap)*incAndCap)
print("capital at the end of the week : {:.2f} usd, ".format(finalCap),"(",finalCap, " to be exact)", sep='')

gain = finalCap - capital
print(''' `"When we buy bitcoin with {} USD at the beginning of the week, \
we would earn {:.2f} USD at the end of the week, with an average gain of 12%."` '''.format(capital,gain))

# temperature conversion
fahr = input("Enter temperature in Fahrenheit :")
celc = (5/9) * (int(fahr) - 32)
print("Temperature (C) : {:.1f}".format(celc))

# there should be an easier indexing method ???
inNumber = input("Enter a three digit number :")
total = int(inNumber[0]) + int(inNumber[1]) + int(inNumber[2])
print("The sum of digits in the number is",total)

# hypotenuse calculation
firstSide = int(input("Enter the length of first side of the right angled triangle : "))
secondSide = int(input("Enter the length of second side of the right angled triangle : "))
hypotenuse = ((firstSide**2)+(secondSide**2))**0.5
print("The length of the hypotenuse is",hypotenuse)
