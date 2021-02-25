# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:23:40 2021

@author: LJB
"""

N = int(input())

gw = 0
for i in range(N):
    tf = True
    a = input()
    for j in range(len(a)-1):
        if a[j] != a[j+1]:
            b = a[j+1:]
            if a[j] in b:
                tf = False
                break
    if tf == True:
        gw += 1

print(gw)

# 고민 한 10분쯤 한거같은데 자꾸 잘 안됐음.
# 찾아보고 다음글자와 같지 않은 경우 뒤의 문자들을 새로 저장하여
# 이래저래 하는 방법을 캐치한 후 안보고 열시미 짜봄.