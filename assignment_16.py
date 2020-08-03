#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:43:53 2020

@author: illcare
"""

import pandas as pd
import numpy as np

theArray = np.array([[2, 3, 5, 7, 11, 13, 17, 19, 23, 29], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]]).T
theFrame = pd.DataFrame(theArray,
                   columns=['prime numbers', 'fibonacci numbers'],
                   index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(theFrame)