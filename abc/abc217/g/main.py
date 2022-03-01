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

n,m = map(int,input().split())
mod = 998244353

dp = [0] * (n+1)
dp[0] = 1
for i in range(n):
    dp2 = [0] * (n+1)
    for j in range(i+1):
        dp2[j+1] += dp[j]
        dp2[j+1] %= mod
        dp2[j] += dp[j] * max(0,j-(i//m))
        dp2[j] %= mod
    dp,dp2 = dp2,dp

print('\n'.join(map(str,dp[1:])))

