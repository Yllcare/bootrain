#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:49:05 2020

@author: illcare
"""

# # sum of ...
# my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]
# my_list.sort()
# print(my_list[0]+my_list[1]+my_list[-2]+my_list[-1])

# # 
# names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", 
#           "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra"]

# scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]
# name = input("Enter student's name :")
# print("score of", name, "is", scores[names.index(name)])

# #
# sortedScores = scores.copy()
# sortedScores.sort()
# print("highest score is", sortedScores[-1], "and only", sortedScores.count(sortedScores[-1]), "student(s) got it")

# 4
months = ["January", "February", "March", "April", "May", "June", 
"July", "August", "September", "October", "November", "December"]
dayCount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
together = [months, dayCount]

# 5
spring=[together[0][2:5],together[1][2:5]]
summer=[together[0][5:8],together[1][5:8]]
fall=[together[0][8:11],together[1][8:11]]
winter=[[together[0][-1],*together[0][0:2]],[together[1][-1],*together[1][0:2]]]

# 6
print("\nsummer has", summer[1][0]+summer[1][1]+summer[1][2], "days")