#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 02:33:36 2020

@author: illcare
"""
import matplotlib.pyplot as plt
import numpy as np
#%% this is how you create cell blocks in spyder
x = np.arange(-3*np.pi, 3*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.show()
#%%
fig, ax = plt.subplots() # created a figure and a set of subplots.
# Now we have an axes named ax. We can add plots to this axes.
ax.plot(x, y, color = '#FF0000')
plt.show()