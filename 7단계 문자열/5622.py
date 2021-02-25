# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:51:43 2021

@author: LJB
"""

num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()
T = 0

for i in range(len(a)):
    for j in num:
        if a[i] in j:
            T += num.index(j) + 3

print(T)

# 모르는 건 없었으나 이런 아이디어가 떠오르지 않아 찾아보고 감잡고 안보고 썻음.
# 아이디어 잘 떠올리는게 중요하겠구나 느꼈음.