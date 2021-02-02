import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = input()
K = int(input())

len_n = len(n)

dp = []
for _ in range(len_n + 1):
    dp.append([[0] * 4 for __ in range(2)])

# dp = [ [[0] * K] for __ in range(2)  for _ in range(len_n + 1)]
dp[0][1][0] = 1

for i in range(1, len_n+1):
    now = int(n[i-1])

    dp[i][0][0] = 1
    for j in range(1,4):
        dp[i][0][j] = dp[i-1][0][j] + dp[i-1][0][j-1] * 9
        if(now == 0):
            dp[i][1][j] = dp[i-1][1][j]
        else:
            dp[i][0][j] += dp[i-1][1][j]
            dp[i][0][j] += dp[i-1][1][j-1] * (now-1)
            dp[i][1][j] = dp[i-1][1][j-1]

print(dp[-1][0][K] + dp[-1][1][K])
