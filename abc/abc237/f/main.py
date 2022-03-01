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

dp = [[[0] * (m+1) for i in range(m+1)] for j in range(m+1)]
dp[-1][-1][-1] = 1

for _ in range(n):
    dp2 = [[[0] * (m+1) for i in range(m+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(m+1):
            for k in range(m+1):
                if dp[i][j][k] == 0:
                    continue
                for x in range(m):
                    if x <= i:
                        dp2[x][j][k] += dp[i][j][k]
                        dp2[x][j][k] %= mod
                    elif x <= j:
                        dp2[i][x][k] += dp[i][j][k]
                        dp2[i][x][k] %= mod
                    elif x <= k:
                        dp2[i][j][x] += dp[i][j][k]
                        dp2[i][j][x] %= mod
    dp,dp2 = dp2,dp

ans = 0
for i in range(m+1):
    for j in range(m+1):
        for k in range(m):
            ans += dp[i][j][k]
            ans %= mod
print(ans)
