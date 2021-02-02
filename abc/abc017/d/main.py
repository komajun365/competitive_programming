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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,*f = map(int,read().split())
mod = 10**9 + 7

dp = [0] * (n+1)
dp_cs = [0] * (n+2)
dp[0] = 1
dp_cs[0] = 1

l = -1
latest = [0] * (m+1)
for i,fi in enumerate(f,1):
    l = max(l, latest[fi]-1)
    dp[i] = (dp_cs[i-1] - dp_cs[l]) % mod
    dp_cs[i] = (dp_cs[i-1] + dp[i]) % mod
    latest[fi] = i

print(dp[-1])
# print(dp)
# print(dp_cs)
