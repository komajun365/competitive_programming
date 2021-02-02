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


a,b,c,d = map(int,input().split())
mod = 998244353

dp = [[0] *(d+1) for _ in range(c+1)]
dp[a][b] = 1

for i in range(1,c+1):
    for j in range(1,d+1):
        dp[i][j] += dp[i-1][j]*j + dp[i][j-1]*i - dp[i-1][j-1]*(i-1)*(j-1)
        dp[i][j] %= mod

print(dp[-1][-1])

# print(dp)
