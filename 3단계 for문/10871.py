# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:08:06 2021

@author: LJB
"""

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=' ')