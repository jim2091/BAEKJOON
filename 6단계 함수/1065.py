# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:13:41 2021

@author: LJB
"""

def hansu():
    N = int(input())
    hansu = 0
    
    for i in range(1, N+1):
        if i < 100:
            hansu += 1
        else:
            n = list(map(int, str(i)))
            if n[0] - n[1] == n[1] - n[2]:
                hansu += 1
    print(hansu)

hansu()
