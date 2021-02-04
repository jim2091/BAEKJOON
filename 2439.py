# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:50:29 2021

@author: LJB
"""

N = int(input())

for i in range(N):
    print(' '*(N-1-i) + '*'*(i+1))
# + 말고 , 를 쓰면 빈칸이 하나 생겨서 틀림.