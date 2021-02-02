import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

N = int(input())
s = input()

MOD = 10**9 + 7

dp =  [[0] * N for i in range(N)]

dp[0][0] = 1
for i in range(1,N):
    if( s[i-1] == '<'):
        tmp = 0
        for j in range(i+1):
            dp[i][j] = tmp
            tmp += dp[i-1][j]
            tmp = tmp % MOD
    else:
        tmp = 0
        for j in range(i-1,-1,-1):
            tmp += dp[i-1][j]
            tmp = tmp % MOD
            dp[i][j] = tmp

ans = sum(dp[N-1]) % MOD
print(ans)
