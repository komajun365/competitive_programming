# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read

n,m,*data = map(int,read().split())
mod = 10**9+7

rlx = [[] for _ in range(n+1)]
it = iter(data)
for l,r,x in zip(it,it,it):
    rlx[r].append([l,x])

dp = [[1]]

for i in range(1,n+1):
    next = [[0] * (i+1) for _ in range(i+1)]

    for j in range(i):
        for k in range(i):
            next[j][k] = (next[j][k] + dp[j][k]) % mod
            next[i-1][j] = (next[i-1][j] + dp[j][k]) % mod
            next[i-1][k] = (next[i-1][k] + dp[j][k]) % mod
    
    for l,x in rlx[i]:
        if x == 1:
            for j in range(l,i):
                for k in range(i):
                    next[j][k] = 0
        elif x == 2:
            for j in range(l):
                for k in range(i):
                    next[j][k] = 0
            for j in range(l,i):
                for k in range(l,i):
                    next[j][k] = 0
        else:
            for j in range(i):
                for k in range(l):
                    next[j][k] = 0
    
    dp,next = next,dp

ans = 0
for i in range(n+1):
    ans += sum(dp[i])
    ans %= mod

print(ans)
# print(dp)
