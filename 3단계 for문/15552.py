# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 12:41:12 2021

@author: LJB
"""

import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
# 문제에서 연산 속도의 문제로 sys.stdin.readline()을 쓰라고 했으나 주피터나 스파이더에서는 이게 실행되지는 않는다고 함.
# 결과는 정답이넹..