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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,*ab = map(int,read().split())
a = ab[:n+1]
b = ab[n+1:]
mod = 10**9+7

ans = 0
a_tot = sum(a) % mod
for ai,bi in zip(a[::-1],b):
    ans += a_tot * bi
    ans %= mod
    a_tot -= ai
    a_tot %= mod
print(ans)
