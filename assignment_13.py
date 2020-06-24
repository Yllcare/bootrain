#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:18:45 2020

@author: illcare
"""

import numpy as np
# 1
sqrMt = [40,60,55,65,85,125,35,95,185,220]
rooms = [2,3,3,3,4,4,2,4,5,6]
price = [100,200,190,210,320,350,120,310,450,550]
all = np.array([sqrMt,rooms,price])
# 2
all = np.transpose(all)
# 3
print("\nthe array has the information of",np.shape(all)[0],"houses with",np.shape(all)[1],"features on every line")
print(all)
# 4
rows = int(input("input number of rows:"))
columns = int(input("input number of columns:"))
new = np.ones([rows,columns])
new[1:np.shape(new)[0]:2, 1:np.shape(new)[1]:2] = 0
print("\nmatrix of ones with zeros on where rows and columns are both even\n",new)
