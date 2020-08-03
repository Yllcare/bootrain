#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:46:45 2020

@author: illcare
"""

import numpy as np
lddData = np.genfromtxt('/home/illcare/Downloads/pythonFilesCodesEtc/earthq_slced.csv',delimiter=',') # ,skip_header=1
#
print('mean values:', np.mean(lddData,axis = 0))
print('deviation values:', np.std(lddData,axis = 0))
#
subtee = [1, 25, 25, 10, 4]
subtData = lddData-subtee
#
multpData = subtData * 2