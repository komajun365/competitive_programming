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

dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    dp2 = [[0] * (k+1) for _ in range(n+1)]
    for j in range(i):
        for l in range(k+1):
            if l+j*2 <= k:
                # 1個置く
                dp2[j][l+j*2] += dp[j][l] * (j*2+1)
                dp2[j][l+j*2] %= mod
            if l+j*2+2 <= k:
                # 置かない
                dp2[j+1][l+j*2+2] += dp[j][l]
                dp2[j+1][l+j*2+2] %= mod
            if j > 0 and l+(j-1)*2 <= k:
                # 2個置く
                dp2[j-1][l+(j-1)*2] += dp[j][l] * j**2
                dp2[j-1][l+(j-1)*2] %= mod
    dp,dp2 = dp2,dp

print(dp[0][k])
