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

d = int(input())
n = input()
mod = 10**9+7

dp = [[0] * d for _ in range(2)]
dp[0][0] = 1
for x in n:
    x = int(x)
    dp2 = [[0] * d for _ in range(2)]
    for i in range(10):
        for j in range(d):
            go = (j + i) % d
            if i < x:
                dp2[1][go] += dp[0][j] + dp[1][j]
            elif i == x:
                dp2[0][go] += dp[0][j]
                dp2[1][go] += dp[1][j]
            else:
                dp2[1][go] += dp[1][j]
            dp2[0][go] %= mod
            dp2[1][go] %= mod
    dp,dp2 = dp2,dp
    # print(dp)

ans = dp[0][0] + dp[1][0] - 1
ans %= mod

print(ans)
