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

n,k,x,y = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)

# ベホイミのほうが効率が良い最大人数
upper = y//x
if(upper < n):
    bhm = 1 + (a[upper]-1-1)//k
else:
    upper = n
    bhm = 0

ans = y*bhm
for i in a[:upper]:
    remain = i - k*bhm
    if(remain<=0):
        continue
    ans += (1+(remain-1-1)//k) * x

print(ans)
