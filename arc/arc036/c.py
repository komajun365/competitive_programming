# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
s = input()
mod = 10**9+7

ans = 0

for d in range(-k,1):
    dp = [[0] * (k+2) for _ in range(2)]
    if(d==0):
        dp[1][0] = 1
    else:
        dp[0][-d] = 1
    for i,si in enumerate(s,1):
        next = [[0] * (k+10) for _ in range(2)]
        if(si!='1'):
            next[1][0] = (dp[0][1] + dp[1][1])%mod
        for j in range(1,k+1):
            if(si!='0'):
                next[0][j] += dp[0][j-1]
                next[1][j] += dp[1][j-1]
            if(si!='1'):
                next[0][j] += dp[0][j+1]
                next[1][j] += dp[1][j+1]
            next[0][j] %= mod
            next[1][j] %= mod
        dp,next = next,dp
    ans += sum(dp[1])

ans %= mod
print(ans)
