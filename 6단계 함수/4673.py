# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:26:35 2021

@author: LJB
"""

def self_num():
    result =  set()
    for i in range(1, 10001):
        num = i
        for j in str(i):
            num += int(j)
        result.add(num)
    for k in range(1, 10001):
        if k not in result:
            print(k)

self_num()
