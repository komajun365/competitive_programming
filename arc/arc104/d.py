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

n,k,m = map(int,input().split())
n2 = (n+1)//2
w = (n * (n+1)//2) * k
dp = [[0] * (w+1) for _ in range(n+1)]

for j in range(1,k+1):
    dp[1][j] = 1

for i in range(2,n+1):
    dp[i][i] = 1
    for j in range(i+1,w+1):
        dp[i][j] = dp[i-1][j-1] + dp[i][j-i]
        if(i > k):


ans = [0] * (n+1)
for i in range(1,n+1):
    for
