# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:23:51 2021

@author: LJB
"""

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print('Case #%d: %d + %d = %d'%(i, A, B, A+B))