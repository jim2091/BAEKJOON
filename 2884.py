# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:23:15 2021

@author: LJB
"""

H, M = map(int, input().split())

if M >= 45:
    print(H, M-45)
elif M < 45 and H >= 1:
    print(H-1, M+15)
else:
    print(23, M+15)