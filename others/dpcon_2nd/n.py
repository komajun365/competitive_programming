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
a = list(map(int,input().split()))

cumsum = [0]*(n+1)
for i in range(n):
    cumsum[i+1] = cumsum[i] + a[i]

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(2,n+1):
    for l in range(n+1-i):
        r = l+i
        tmp = 10**20
        for mid in range(l+1,r):
            tmp = min(tmp, dp[l][mid]+dp[mid][r])
        dp[l][r] = tmp + cumsum[r] - cumsum[l]

print(dp[0][n])
