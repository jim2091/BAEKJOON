# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 12:58:09 2021

@author: LJB
"""

S = input()

AtoZ = list(range(97, 123))

for i in AtoZ:
    print(S.find(chr(i)))
    
    
# 이번엔 모르는게 많았음. 정답 보고 그냥 그대로 함.
# 아스키코드를 문자로 변환해주는 chr
# find함수는 찾는 문자열이 없을 경우 -1을 출력해줌.