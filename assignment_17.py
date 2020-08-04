#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 02:30:29 2020

@author: illcare
"""

import pandas as pd
import numpy as np

tita = pd.read_csv("train.csv", index_col=0)
survRate30 = np.shape(tita[(tita['Survived'] == 1) & (tita['Age'] < 30)])[0] / np.shape(tita[tita['Survived'] == 1])[0]
print('Survival rate of passengers under the age of 30 is {:.2f} percent'.format(survRate30*100))
#
survRateSx = np.shape(tita[(tita['Survived'] == 1) & (tita['Sex'] == 'female')])[0] / np.shape(tita[(tita['Survived'] == 1) & (tita['Sex'] == 'male')])[0] 
print('Survival rate of female passengers to male passengers is {:.2f}'.format(survRateSx))