#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 01:55:24 2020

@author: illcare
"""

import numpy as np
# import pandas as pd
whole = np.genfromtxt('/home/illcare/Downloads/pythonFilesCodesEtc/eq/Earthquakes.csv',delimiter=',') # ,skip_header=1
#
slc = whole[0:20,[2, 4, 5, 6, 11]] # columns 3, 5, 6, 7, 12
#
thrs=[np.where(slc[:,-1]>=4.5)]
print('rows numbers with a value of 4.5 or higher in the last column:', thrs[0][0])
#
slc[0,]=1
#
np.savetxt('earthq_slced.csv', slc, delimiter=',')