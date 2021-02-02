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

n,*xyz = map(int,read().split())

it= iter(xyz)
xyz = [[x,y,z] for x,y,z in zip(it,it,it)]

inf = 10**10
bit_n = 2**(n-1)
dp = [[inf] * bit_n for _ in range(n-1)]

cost = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(i==j):
            continue
        cost[i][j] = abs(xyz[i][0] - xyz[j][0]) + abs(xyz[i][1] - xyz[j][1]) + max(0,xyz[j][2] - xyz[i][2])

for i in range(n-1):
    dp[i][1<<i] = cost[0][i+1]

for j in range(0,bit_n):
    for i in range(n-1):
        if(dp[i][j] == inf):
            continue
        for bi in range(n-1):
            if(j >> bi)&1:
                continue
            dp[bi][j | (1<<bi)] = min(dp[bi][j | (1<<bi)], dp[i][j] + cost[i+1][bi+1])

ans = inf
for i in range(n-1):
    ans = min(ans,dp[i][-1] + cost[i+1][0])
print(ans)
