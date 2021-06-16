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

n,x = map(int,input().split())
a = list(map(int,input().split()))
a = a[-1:] + a

ans = 10**9 * n
for i in range(n):
    ans = min(ans,sum(a[1:])+i*x)
    for j in range(n,0,-1):
        a[j] = min(a[j],a[j-1])
    a[0] = a[-1]
print(ans)
