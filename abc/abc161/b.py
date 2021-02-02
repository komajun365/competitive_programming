# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
a = list(map(int,input().split()))
limit = 1+(-1+sum(a))//(4*m)

cnt=0
for i in a:
    if(i>=limit):
        cnt+=1

if(cnt>=m):
    print('Yes')
else:
    print('No')
