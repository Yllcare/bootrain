#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:55:00 2020

@author: illcare
"""

class item:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price
        
class customer(item):
    def __init__(self, item_name, price, customer_id, phone_number):
        item.__init__(self, item_name, price)
        self.customer_id = customer_id
        self.phone_number = phone_number
        
    def purchase(self, amount):
        total = self.price * amount
        print("total price for", amount, self.item_name, "is", total)
        
sold_item = "chocolate bar"
sold_price = 2 # dollars
sold_cust = "Roger"
sold_phone = "+90 569 565 0555"

sss = customer(sold_item, sold_price, sold_cust, sold_phone)
sss.purchase(20)