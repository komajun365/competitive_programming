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

n,l = map(int,input().split())
mod = 10**9 + 7
dp = [0] * (n+1)
dp[0] = 1
for i in range(1,n+1):
    dp[i] = dp[i-1]
    if i >= l:
        dp[i] += dp[i-l]
        dp[i] %= mod
print(dp[-1])