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

n,*abc = map(int,read().split())

dp = [[0] * 3 for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + abc[(i-1)*3]
    dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + abc[(i-1)*3+1]
    dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + abc[(i-1)*3+2]

print(max(dp[-1]))
