import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,w = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]

dp = [[10**11] * (n * (10**3) + 1) for _ in range(n+1)]

for i in range(1,n+1):
    dp[i-1][0] = 0
    w_temp, v_temp = wv[i-1]
    for j in range(1, (n*10**3)+1):
        if(j >= v_temp):
            dp[i][j] = min(dp[i-1][j],
                            dp[i-1][j-v_temp] + w_temp)
        else:
            dp[i][j] = dp[i-1][j]

last = dp[-1]
ans = 0
for j in range((n*10**3)+1):
    if(last[j] <= w):
        ans = j

print(ans)
