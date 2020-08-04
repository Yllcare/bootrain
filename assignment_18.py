#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:19:57 2020

@author: illcare
"""

import pandas as pd
# countries = pd.read_csv("Countries.csv", index_col=0)
# print(   countries.groupby(by='Continent').agg({"Life Expectancy" : ['mean', "count"],"Population" : ['mean', "sum"] })   )
# print(   countries.groupby(by='Continent')[["Population","Life Expectancy"]].agg(["sum","mean"])   )

tita = pd.read_csv("train.csv", index_col=0)
meanAge_Sx = tita.groupby(by=['Sex','Pclass'])[['Age']].agg(['mean','count'])
display('Mean age of passengers by gender and ticket class',meanAge_Sx)
#
byPort = tita.groupby(by="Embarked")
for group_name, group in byPort :
    display(group)
    print(group_name)
    
# C = Cherbourg, Q = Queenstown, S = Southampton