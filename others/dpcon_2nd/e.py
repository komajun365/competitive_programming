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
v_max = 10**5

dp = [[W+1] * (v_max+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1):
    w,v = wv[(i-1)*2:i*2]
    dp[i][0] = 0
    for j in range(1,v_max+1):
        dp[i][j] = dp[i-1][j]
        if(j >= v):
            dp[i][j] = min(dp[i][j], dp[i-1][j-v] + w)

for j in range(v_max,-1,-1):
    if(dp[-1][j] <= W):
        print(j)
        exit()
