#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:42:41 2020

@author: illcare
"""

first =("""\nMürdüm eriği
          çiçek açmıştır.
— ilkönce zerdali çiçek açar
                  mürdüm en sonra —""")
second = """Sevgilim,
çimenin üzerine
diz üstü oturalım
karşı-be-karşı.
Hava lezzetli ve aydınlık
— fakat iyice ısınmadı daha —
çağlanın kabuğu
                yemyeşil tüylüdür
                                    henüz yumuşacık…
Bahtiyarız
            yaşayabildiğimiz için."""

with open("BAD.txt",'w') as bad:
    bad.write(first)
    
with open("BAD.txt",'a') as bad:
    bad.write(second)
    
with open("BAD.txt",'r') as bad:
    all = bad.read()
    
print(all)