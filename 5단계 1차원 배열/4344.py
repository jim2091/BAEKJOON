# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:22:35 2021

@author: Leejeongbin
"""


C = int(input())

for i in range(C):
    case_lst = list(map(int, input().split()))
    
    avg = sum(case_lst[1:])/case_lst[0]
    
    cnt = 0
    for j in case_lst[1:]:
        if j > avg:
            cnt += 1
    rate = cnt / case_lst[0] * 100
    print('{:.3f}%'.format(rate))
    
# 값을 소수점 몇째자리까지 출력하는 방법 여러가지가 있었음.
# count는 cnt로 많이들 줄여서 사용함.
# 알고리즘 주요 형태는 혼자 잘 생각해냈고 마지막 프린트부분때문에 찾다가 보고 참고하여 약간 수정되긴 했음.