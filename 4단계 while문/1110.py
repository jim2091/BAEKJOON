# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:12:39 2021

@author: LJB
"""

N = int(input())
check = N
count = 0
temp = 0

while True:
    temp = N//10 + N%10
    NN = (N%10)*10 + temp%10
    count += 1
    N = NN
    if NN==check:
        break

print(count)

# 검색 해보고서야 해결.
# 처음엔 str의 인덱싱 같은 방법으로 해보려 했었음. 근데 쉽지 않아보이고 너무 복잡할거 같았음.
# temp와 같은 개념을 활용한 while문 활용법 기억.