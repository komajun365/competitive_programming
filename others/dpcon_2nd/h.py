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

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

h,w= map(int,readline().split())
a = read().split()
mod = 10**9+7

dp = [[0]*w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if(a[i][j] == '#'):
            continue
        if(i!=0):
            dp[i][j] += dp[i-1][j]
        if(j!=0):
            dp[i][j] += dp[i][j-1]
        dp[i][j] %= mod
print(dp[-1][-1])

# print(dp)
