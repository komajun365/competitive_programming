# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,x,d = map(int,input().split())

if(d==0)&(x==0):
    print(1)
    exit()

if(d==0):
    print(n+1)
    exit()

if(x=0):
    print(1 + (n-1)*n//2)
    exit()

if(d<0):
    x = x + (n-1)*d
    d = abs(d)

if(x>=0):
    for i in range()
