# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n,m,x = map(int,input().split())
ca = [list(map(int,input().split())) for _ in range(n)]

inf = 10**10
ans = inf
for i in range(2**n):
    und = [0] * m
    cost = 0
    for j in range(n):
        if((i>>j)&1):
            cost += ca[j][0]
            for k in range(m):
                und[k] += ca[j][k+1]
    if(min(und) >= x):
        ans = min(ans,cost)

if(ans==inf):
    print(-1)
else:
    print(ans)
