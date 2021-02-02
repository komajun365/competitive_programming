import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

div = (10**9)+7
h,w = map(int, input().split())

dp = [[0]*(w+1) for _ in range(h+1)]

for i in range(h):
    a_h = input()
    for j in range(w):
        if((i==0) & (j==0)):
            dp[i+1][j+1] = 1
        else:
            if(a_h[j] == '.'):
                dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1])%div

print(dp[h][w])
