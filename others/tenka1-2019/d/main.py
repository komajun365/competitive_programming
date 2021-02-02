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
n,*a = map(int,read().split())
mod = 998244353

tot = sum(a)
dp = [0] * (tot+1)
dp[0] = 1

for ai in a:
    next = [0] * (tot+1)
    for j in range(tot+1):
        next[j] += dp[j]*2
        if j >= ai:
            next[j] += dp[j-ai]
        next[j] %= mod
    dp,next = next,dp

ans = pow(3,n,mod)
for i in range((tot+1)//2, tot+1):
    ans -= dp[i] * 3

ans %= mod

if tot%2 == 0:
    dp = [0] * (tot+1)
    dp[0] = 1

    for ai in a:
        next = [0] * (tot+1)
        for j in range(tot+1):
            next[j] += dp[j]
            if j >= ai:
                next[j] += dp[j-ai]
            next[j] %= mod
        dp,next = next,dp
    
    ans += dp[tot//2] * 3

ans %= mod
print(ans)
# print(dp)

