import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
abc = [list(map(int, input().split())) for i in range(n)]

dp = [[0,0,0] for _ in range(n)]
dp[0] = abc[0]

for i in range(1,n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + abc[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + abc[i][1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + abc[i][2]

ans = max(dp[n-1])

print(ans)
