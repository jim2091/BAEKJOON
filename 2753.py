# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:10:26 2021

@author: LJB
"""

a = int(input())

if a % 4 == 0:
    if a % 400 == 0:
        print('1')
    elif a % 100 == 0:
        print('0')
    else:
        print('1')
else:
    print('0')