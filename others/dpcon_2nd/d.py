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

n,W,*wv = map(int,read().split())

dp = [[0] * (W+1) for _ in range(n+1)]

for i in range(1,n+1):
    w,v = wv[(i-1)*2:i*2]
    for j in range(1,W+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        if(j >= w):
            dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)

print(dp[-1][-1])
