# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s,l,r = map(int,input().split())
if(s<l):
    print(l)
elif(s>r):
    print(r)
else:
    print(s)
