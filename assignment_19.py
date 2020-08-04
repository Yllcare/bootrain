#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 00:10:05 2020

@author: illcare
"""
import pandas as pd
import numpy as np

tita = pd.read_csv("train.csv", index_col=0)
test = pd.read_csv("test.csv", index_col=0)
allData = pd.concat([tita, test])
print('length of dataFrame is', allData.shape[0])
# all_countries = pd.concat([countries, new_countries], ignore_index=True)
mendou = {'id':[1001,1001,1002,1002,1003,1004,1005,1006,1007,1007,1008,1008],
          'age':[63,37,41,56,57,57,56,44,52,57,54,48],
          'sex':['Male','Male','Female','Male','Female','Male','Female','Male','Male','Male','Male','Female'],
          'beats':[145,130,130,120,120,140,140,120,172,150,140,150],
          'chol':[233,250,204,236,354,192,294,263,199,168,239,264]}
miniMend = {'id':[1001,1002,1004,1005,1007,1008],'target':[0,1,0,1,0,1]}

mendouFrame = pd.DataFrame(mendou)
# mendouFrame.set_index('id', inplace=True)
# miniFrame = pd.DataFrame(miniMend,index='id')
miniFrame = pd.DataFrame(miniMend)

mergIn = pd.merge(mendouFrame, miniFrame, left_on='id', right_on='id', how = "inner")
mergOut = pd.merge(mendouFrame, miniFrame, left_on='id', right_on='id', how = "outer")
mergLeft = pd.merge(mendouFrame, miniFrame, left_on='id', right_on='id', how = "left")
mergRight = pd.merge(mendouFrame, miniFrame, left_on='id', right_on='id', how = "right")
print('length of inner merge:',np.shape(mergIn)[0],'\nlength of outer merge:',np.shape(mergOut)[0],
      '\nlength of left merge:',np.shape(mergLeft)[0],'\nlength of right merge:',np.shape(mergRight)[0])