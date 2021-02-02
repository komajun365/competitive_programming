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
y = list(map(int,input().split()))

dp = [[0] * (10**4+1) for _ in range(1+n)]
# dp[0][0] = 0

for i in range(1,n+1):
    for j in range(10**4+1):
        if(j==0):
            dp[i][j] = dp[i-1][j] + abs(j-y[i-1])
        else:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j] + abs(j-y[i-1]))

print(min(dp[i]))

# for i in dp:
#     print(i[:15])

'''
dp[i][j]:= i番目の数字を見て、最後がj以下になってる時の最小コスト

'''
