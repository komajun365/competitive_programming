# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
days = 'SUN,MON,TUE,WED,THU,FRI,SAT'.split(",")
print(7 - days.index(s))
