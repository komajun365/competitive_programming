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

n,h,d = map(int,input().split())
mod = 10**9 + 7

sum_fac = 0
tmp_fac = 1
for i in range(1,n+1):
    tmp_fac *= i
    tmp_fac %= mod
    sum_fac += tmp_fac
    sum_fac %= mod

dp = [0] * h
dp[0] = tmp_fac
tot = tmp_fac
for i in range(1,h):
    dp[i] = sum_fac * tot % mod
    tot += dp[i]
    if i >= d:
        tot -= dp[i-d]
    tot %= mod

print(tot)


