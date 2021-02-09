# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:57:00 2021

@author: LJB
"""

a = []
for i in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)