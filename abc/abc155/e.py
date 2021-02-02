import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = input()
len_n = len(n)

dp = [[0]*2 for _ in range(len_n + 1)]
dp[0][1] = 1

for i in range(1, len_n+1):
    tmp = int(n[i-1])

    dp[i][0] = min(dp[i-1][0] + tmp, dp[i-1][1] + (10-tmp))
    dp[i][1] = dp[i-1][1] + (9-tmp)
    if(tmp != 9):
        dp[i][1] = min(dp[i][1], dp[i-1][0] + tmp + 1)

ans = min(dp[-1][0], dp[-1][1] + 1)

print(ans)
