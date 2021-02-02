# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
a = list(map(int,input().split()))

cs_l = [0] * (n+2)
cs_r = [0] * (n+2)
for cs,ax in zip([cs_l,cs_r],[a,a[::-1]]):
    for i in range(n):
        cs[i+1] = cs[i] + max(ax[i],0)

cs_r = cs_r[::-1]

ans = 0
center = sum(a[:k])
for i in range(n-k+1):
    ans = max(ans, max(0,center) + cs_l[i] + cs_r[i+k+1])
    if(i==n-k):
        break
    center += a[i+k] - a[i]
print(ans)
