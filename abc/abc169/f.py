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


n,s = map(int,input().split())
a = list(map(int,input().split()))
mod = 998244353

dp = [[0] * (s+1) for _ in range(n+1)]

dp[0][0] = 1
for i in range(1,n+1):
    for j in range(0,s+1):
        dp[i][j] += dp[i-1][j] * 2
        if(j>=a[i-1]):
            dp[i][j] += dp[i-1][j-a[i-1]]
        dp[i][j] %= mod

print(dp[-1][-1])
