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

n,m = map(int,input().split())
mod = 998244353
if(n==1):
    print(1)
    exit()

dp = [0] * (m+1)
dp[0] = 1
for i in range(1,m+1):
    dp[i] += dp[i-1]
    if(i>=n):
        dp[i] += dp[i-n]
    dp[i] %= mod

print(dp[-1])
