# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:11:53 2021

@author: LJB
"""

a = []

for i in range(10):
    a.append(int(input())%42)
b = set(a)
print(len(b))