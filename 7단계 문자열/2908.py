# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:48:05 2021

@author: LJB
"""

A, B = input().split()

A = A[2] + A[1] + A[0]
B = B[2] + B[1] + B[0]

print(max(A, B))