# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:25:51 2021

@author: LJB
"""

a = input().upper()

check = list(set(a))
cnt = []

for i in check:
    cnt.append(a.count(i))
    
if cnt.count(max(cnt)) > 1:
    print('?')

else:
    print(check[cnt.index(max(cnt))])
    
# set 자료형에 들어있는 값을 인덱싱으로 접근하려면 리스트나 튜플의 형태로 변환해주어야함.
# set(a)가 아닌 list(set(a))의 형태로 만든 이유는 오직 그 이유.