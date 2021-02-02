# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,t = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]

ab.sort()

dp = [[0] * (t+1) for _ in range(n+1)]

for i in range(1,n+1):
    a,b = ab[i-1]
    for j in range(1,t):
        if(j < a):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-a] + b)
    dp[i][t] = max(dp[i-1][t], dp[i][t-1], dp[i-1][t-1]+b)

print(dp[-1][-1])
