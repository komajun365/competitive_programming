import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

div = 10**9 + 7

n,k = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(k+1)]
dp[0] = [1]*(n+1)

for i in range(1,k+1):
    for j in range(1, n+1):
        if(i <= a[j-1]):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])%div
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i - a[j-1] - 1][j -1])%div

print(dp[k][n] % div)
