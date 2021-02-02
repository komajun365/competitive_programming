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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

coins = [1,2,5,10,20,50,100,200]
n = len(coins)
target = 200

dp = [[0] * (target+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    for j in range(target+1):
        dp[i][j] = dp[i-1][j]
        if(j >= coins[i-1]):
            dp[i][j] += dp[i][j-coins[i-1]]

print(dp[-1][target])


'''
DPしましょ
'''
