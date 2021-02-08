# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:02:45 2021

@author: LJB
"""

while True:
    A, B = map(int, input().split())
    if A==0 and B==0:
        break
    else:
        print(A+B)