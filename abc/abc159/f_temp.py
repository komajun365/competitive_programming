# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,s = map(int,input().split())
a = tuple(map(int,input().split()))

mod = 998244353

dp = [[0] * (s+1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][0] = (dp[i-1][0] + i) % mod

dp[0][0] = 1

for i in range(1,n+1):
    a_t = a[i-1]
    for j in range(1,s+1):
        dp[i][j] = dp[i-1][j] 
        if(a_t <= j):
            dp[i][j] += dp[i-1][j-a_t]
            dp[i][j] %= mod

print(dp[-1][-1])
print(dp)
