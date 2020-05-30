#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:41:20 2020

@author: illcare
"""

def prime(p,result=True):
    if p==2:
        result=True
    elif p%2==0:
        result=False
    else:
        for i in range(p//2,2,-1):
            if p%i==0:
                result=False
                
    return result


def unique_list(orgList):
    newList = []
    for n in range(len(orgList)):
        if orgList[n:].count(orgList[n])==1:
            newList.append(orgList[n])
            
        newList.sort()
    return newList


def factorial(nu):
    res=1
    for i in range(nu):
        res *= i+1
        
    return res


def perfect(min=1,max=1000):
    perfList=[]
    for n in range(min,max+1): # for every number within the range
        divList=[]
        for m in range(1,n): # using lower numbers as a divisor
            if n%m==0: # i find proper divisors
                divList.append(m) # and make a list out of them
                
        if sum(divList)==n: # if sum of the divisor list equals to the number itself
            perfList.append(n) # then the number is added to perfect number list
        
    return perfList


def pascal(rows):
    tri=[[1],[1,1]]
    if rows<=2:
        result=tri[:rows]
    elif rows>2:
        for n in range(rows-2): # number of rows to be calculated after the second one
            rowList =[1]
            for c in range(n+1): # for every row, cells to be calculated between edges of 1
                app = tri[n+1][c]+tri[n+1][c+1]
                rowList.append(app)
                
            rowList.append(1)
            tri.append(rowList)
        result = tri
        
    return result


