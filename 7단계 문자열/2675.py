# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:16:30 2021

@author: LJB
"""

T = int(input())

for i in range(T):
    R, S = input().split()
    l = len(S)
    P = ''
    for j in range(l):
        P += S[j] * int(R)
    print(P)