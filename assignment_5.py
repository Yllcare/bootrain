#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:47:46 2020

@author: illcare
"""

# 1
days = {1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday",7:"sunday"}
chosen = input("please enter 2 days by their sequence in numbers ;")
key1=int(chosen[0])
key2=int(chosen[1])
days.pop(key1)
days.pop(key2)
print(days.values())

# 2

info = {"names":{"john":{"age":25,"sex":"male"},
                 "lisa":{"age":28, "sex":"female"},
                 "linda":{"age":32, "sex":"non-binary"},
                 "michael":{"age":41, "sex":"male"}
                 }
        }

# 3
info["names"]["michael"].update({
    "child":{
        "karen":{"age":12,"sex":"female"},
        "greg":{"age":7, "sex":"male"}
        }
    })
info["names"]["linda"].update({
    "child":{
        "susan":{"age":6,"sex":"female"}
        }
    })

# 4
print("\nmicheal's kids' names are", list(info["names"]["michael"]["child"].keys())[0], "and", \
      list(info["names"]["michael"]["child"].keys())[1])

