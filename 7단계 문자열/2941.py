# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:15:56 2021

@author: LJB
"""

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

b = input()

for i in a:
    b = b.replace(i, 'a')
    
print(len(b))

# 이건 감도 못잡았었음.
# replace함수도 써본적이 없었던 것 같음.
# 알파벳의 수를 세는 것이기 때문에 여러 문자의 합으로 표현되는
# 크로아티아 알파벳을 임의의 길이 하나의 문자(여기선 'a')로 바꾸어줌으로써
# 문제를 해결.