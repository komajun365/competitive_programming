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

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for l in range(n+1-i):
        r = l+i
        dp[l][r] = max(a[l] - dp[l+1][r], a[r-1]-dp[l][r-1])

print(dp[0][n])
