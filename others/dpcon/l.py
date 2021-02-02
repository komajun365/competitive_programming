import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][(n-1)-i] = a[i]

for i in range(n-2, -1, -1):
    for j in range(i+1):
        dp[j][i-j] = max( a[j] - dp[j+1][i-j],
                            a[-(1+i-j)] - dp[j][i-j+1])

print(dp[0][0])
