# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:03:22 2021

@author: LJB
"""

a = int(input())
b = int(input())
c = int(input())
d = list(str(a*b*c))

for i in range(10):
    print(d.count(str(i)))