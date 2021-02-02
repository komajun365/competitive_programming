import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

h, n  = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]

dp = [10**10] * (h+1)
dp[0] = 0

for i in range(1,h+1):
    for j in range(n):
        if(i >= ab[j][0]):
            dp[i] = min(dp[i], dp[ i - ab[j][0]]+ ab[j][1])
        else:
            dp[i] = min(dp[i], dp[0] + ab[j][1])

print(dp[h])
