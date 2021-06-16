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

n,k = map(int,input().split())
mod = 10**9+7

dp = [[0,0] for _ in range(n)]
dp[0] = [1,1]
tot = 1
for i in range(1,n):
    if i >= k-1:
        dp[i][0] = (tot - dp[i-1][1]) % mod
        dp[i][1] = (tot - dp[i-(k-1)][0]) % mod
    else:
        dp[i][0] = (tot - dp[i-1][1]) % mod
        dp[i][1] = tot
    tot += dp[i][1]
    tot %= mod
print(dp[-1][-1])