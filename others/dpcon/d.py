import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n, w = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]* (w+1) for _ in range(n+1)]

for i in range(1, n+1):
    w_temp, v_temp = wv[i-1]
    for j in range(1,w+1):
        if(j >= w_temp):
            dp[i][j] = max(dp[i-1][j],
                            dp[i-1][j-w_temp] + v_temp)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][w])
