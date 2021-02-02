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

dp = [[] for _ in  range(n+1)]
for i in range(n+1):
    dp[i] = [[-1] * (n+1) for j in range(n+1)]

dp[0][0][0] = 0

for i in range(n+1):
    for j in range(n+1):
        if(i+j > n):
            break
        for k in range(n+1):
            if(i+j+k > n):
                break
            if(i==j==k==0):
                continue
            res = n
            if(i>0):
                res += i * dp[i-1][j+1][k]
            if(j>0):
                res += j * dp[i][j-1][k+1]
            if(k>0):
                res += k * dp[i][j][k-1]
            res /= (i+j+k)
            dp[i][j][k] = res

print(dp[a.count(3)][a.count(2)][a.count(1)])
