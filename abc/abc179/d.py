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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k,*data = list(map(int,read().split()))
mod = 998244353

dp = [[0] * (n) for _ in range(k+1)]
dp[0][0] = 1

for i in range(1,k+1):
    l,r = data[i*2-2:i*2]
    route = 0
    dp[i][0] = 1
    for j in range(1,n):
        if(j >= l):
            route += dp[i][j-l] + dp[i][j-l]
        if(j > r):
            route -= dp[i][j-r-1] + dp[i][j-l]
        route %= mod
        dp[i][j] = (route + dp[i-1][j])%mod

print(dp[-1][-1])

for i in dp:
    print(i)
