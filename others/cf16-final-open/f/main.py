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

# 数え上げpdfで読んだ記憶がある

n,m = map(int,input().split())
mod = 10**9 + 7

# dp[i][j] := i個の町に到達済み、かつ、先頭の強連結成分のサイズがj
dp = [[0] * (n+1) for _ in range(n+1)]
dp[1][1] = 1

for _ in range(m):
    dp2 = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp2[i][j] += dp[i][j] * (i-j)
            dp2[i][j] %= mod
            dp2[i][i] += dp[i][j] * j
            dp2[i][j] %= mod
            if i != n:
                dp2[i+1][j] += dp[i][j] * (n-i)
                dp2[i+1][j] %= mod
    dp,dp2 = dp2,dp

ans = dp[-1][-1]
print(ans)

