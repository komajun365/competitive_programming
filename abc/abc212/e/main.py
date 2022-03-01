# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read

n,m,k,*uv = map(int,read().split())
mod = 998244353

dp = [0] * n
dp[0] = 1
for _ in range(k):
    tot = sum(dp) % mod
    dp2 = [tot] * n
    for i in range(n):
        dp2[i] -= dp[i]
        dp2[i] %= mod
    it = iter(uv)
    for u,v in zip(it,it):
        u -= 1
        v -= 1
        dp2[u] -= dp[v]
        dp2[u] %= mod
        dp2[v] -= dp[u]
        dp2[v] %= mod
    dp,dp2 = dp2,dp
    # print(dp)

print(dp[0])
