# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
p = list(map(float,input().split()))
# p = list(map(lambda x: int(x[2:]),input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    pi = p[i]
    for j in range(n):
        dp[i+1][j] += dp[i][j] * (1-pi)
        dp[i+1][j+1] += dp[i][j] * pi

ok = 0
ng = 0
for j in range(0,n+1):
    if(j <= n//2):
        ng += dp[-1][j]
    else:
        ok += dp[-1][j]

print(ok/(ng+ok))
