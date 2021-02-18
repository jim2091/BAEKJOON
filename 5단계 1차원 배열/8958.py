# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:39:33 2021

@author: Leejeongbin
"""


N = int(input())

temp = 'X'
temp_score = 0
score = 0
    
for i in range(N):
    a = input()
    b = len(a)
    for j in range(b):
        c = a[j]
        if c == 'X':
            temp_score = 0
            temp = c
        elif c == 'O':
            score += 1
            if c == temp:
                temp_score += 1
                score += temp_score
            temp = c
    print(score)
    score = 0
    temp = 'X'
    temp_score = 0
    
# 쓸데없이 복잡한거 같다. 더 간단하게 가능했을 것. 그냥 생각나는대로 바로 썼으므로 답안을 통해 개선점 찾아보기
    
'''
# 더 쉬운 다른 답

a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    c = 1
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)

# 굳이 temp를 만들어서 매번 초기화 해주며 더하기 보다 더하는 순서를 조절해 필요없이 가능.
# 문자열을 받아서 list로 만들면 각 글자가 따로 각각 하나의 요소로 리스트에 들어간다는걸 기억하자.    
'''

