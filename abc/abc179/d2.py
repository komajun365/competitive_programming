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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k,*data = list(map(int,read().split()))
mod = 998244353

dp = [0] * n
dp[0] = 1
route = 0
for j in range(1,n):
    for i in range(k):
        l,r = data[i*2:i*2+2]
        if(j >= l):
            route += dp[j-l]
        if(j > r):
            route -= dp[j-r-1]
        route %= mod
    dp[j] += route


print(dp[-1])
# print(dp)
