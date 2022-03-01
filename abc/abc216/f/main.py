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

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mod = 998244353

ab = [[ai,bi] for ai,bi in zip(a,b)]
ab.sort()

dp = [0] * 5001
dp[0] = 1
ans = 0
for ai,bi in ab:
    for j in range(5000):
        if j+bi > ai:
            break
        ans += dp[j]
    ans %= mod
    for j in range(5000-bi,-1,-1):
        dp[j+bi] += dp[j]
        dp[j+bi] %= mod

print(ans)