# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b,c,d = map(int,input().split())
ta = 1 + (a-1)//d
ao = 1 + (c-1)//b
if(ta < ao):
    print('No')
else:
    print('Yes')
