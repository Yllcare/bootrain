#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:11:23 2020

@author: illcare
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

covData = pd.read_csv("owid-covid-data.csv", index_col=0)
countries = ['Spain','France','Germany','Italy']
covDataCoun = covData[covData['location'].isin(countries)]# & (covData['date'] == "2019-12-31")
slcdData = covDataCoun.groupby('location').tail(100)
#
fig, ax = plt.subplots(1, 2)
fig.suptitle('COVID19 last 100 days visualization', fontsize=16)
font1 = {'family': 'serif', 'color':  'darkred','weight': 'normal','size': 12}
font2 = {'family': 'serif', 'color':  'darkblue','weight': 'normal','size': 8}
lnstyl=["-",":","--","-."]

plt.subplot(1, 2, 1)
for c in countries:
    plt.plot(  slcdData[ (slcdData['location']==c) ]['date'],
             slcdData[ (slcdData['location']==c) ]['total_cases'],
             ls=lnstyl[countries.index(c)] )
    
plt.title('COVID19 cases',fontdict =font1)
plt.legend(countries, fontsize = 8, loc = 4)
plt.xlabel('Date',fontdict =font2)
plt.ylabel('Number of cases',fontdict =font2)
plt.xticks(rotation = 90, fontsize = 3, c='c')
plt.yticks(fontsize = 8)

plt.subplot(1, 2, 2)
for c in countries:
    plt.plot(  slcdData[ (slcdData['location']==c) ]['date'],
             slcdData[ (slcdData['location']==c) ]['total_deaths'],
             ls=lnstyl[countries.index(c)] )
    
plt.title('COVID19 deaths',fontdict =font1)
plt.legend(countries, fontsize = 8, loc = 4)
plt.xlabel('Date',fontdict =font2)
plt.ylabel('Number of deaths',fontdict =font2)
plt.xticks(rotation = 90, fontsize = 3, c='m')
plt.yticks(fontsize = 8)

plt.show()

