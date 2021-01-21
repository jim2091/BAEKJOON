# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:54:58 2021

@author: LJB
"""

a, b = input().split()
a = int(a)
b = int(b)

if abs(a) > 10000 or abs(b) > 10000:
    print('')
elif a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')