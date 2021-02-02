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

'''
67と同じ
'''

n = 15
a = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n)]
dp[0][1] = a[0][0]
for i in range(1,n):
    for j in range(1,i+2):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j-1]

print(max(dp[-1]))
# print(dp)
