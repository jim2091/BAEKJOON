# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:40:49 2021

@author: LJB
"""

N = int(input())

for i in range(N):
    for j in range(i+1):
        print('*', end='')
    print('')