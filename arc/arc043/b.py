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

n,*d = map(int,read().split())
mod = 10**9+7

d.append(0)
d.sort()
dp = [[0] * (n+1) for _ in range(5)]
dp[0][0] = 1
for i in range(1,5):
    l = 0
    tot = 0
    for j in range(1,n+1):
        while(d[l]*2 <= d[j]):
            tot += dp[i-1][l]
            tot %= mod
            l += 1
        dp[i][j] = tot

ans = sum(dp[-1])%mod
print(ans)
