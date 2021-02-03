# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:19:04 2021

@author: LJB
"""

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print('Case #%d:'%i, A + B)