# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:29:56 2021

@author: LJB
"""


a = int(input())
b = input()

b1 = int(b[2])
b2 = int(b[1])
b3 = int(b[0])

c1 = a*b1
c2 = a*b2
c3 = a*b3
d = c1 + c2*10 + c3*100

print(c1)
print(c2)
print(c3)
print(d)