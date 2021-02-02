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
mod = 10**9+7

dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1,n+1):
    ai = a[i-1]
    dp[i][0] = 1
    for j in range(1,k+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
        if(j > ai):
            dp[i][j] -= dp[i-1][j-ai-1]
        dp[i][j] %= mod

print(dp[-1][-1])
