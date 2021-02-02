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


n = 20
dp = [[0]*(n+2) for _ in range(n+2)]
dp[1][1]=1
for i in range(1,n+2):
    for j in range(1,n+2):
        dp[i][j] += dp[i-1][j]+dp[i][j-1]

print(dp[-1][-1])

ans = 1
for i in range(n+1,2*n+1):
    ans *= i

for i in range(1,n+1):
    ans //= i

print(ans)
