# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:16:00 2021

@author: LJB
"""

N = int(input())

a = list(map(int, input().split()))
m = max(a)

for i in range(N):
    a[i] = a[i]/m

print((sum(a)/len(a))*100)