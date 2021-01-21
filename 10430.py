# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:22:35 2021

@author: LJB
"""

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)