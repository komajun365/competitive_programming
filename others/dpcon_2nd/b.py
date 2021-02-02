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

n,k = map(int,input().split())
h = list(map(int,input().split()))

dp = [10**10] * n
dp[0] = 0
for i in range(1,n):
    for j in range(max(0,i-k),i):
        dp[i] = min(dp[i], dp[j] + abs(h[i]-h[j]))

print(dp[-1])
