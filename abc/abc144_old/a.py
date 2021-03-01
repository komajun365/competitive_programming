# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b = map(int,input().split())
if(a<=9)&(b<=9):
    print(a*b)
else:
    print(-1)
