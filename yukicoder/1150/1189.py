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
a = list(map(int,input().split()))
mod = 998244353

if(k > 10):
    print(0)
    exit()

cnt = [0] * (2**10)
for ai in a:
    cnt[ai] += 1

dp = [[0] * (2**10) for _ in range(k+1)]
dp[0][0] = 1

for ci in range(2**10):
    for i in range(k):
        for j in range(2**10):        
            if(j & ci)==0:
                dp[i+1][j | ci] += dp[i][j] * cnt[ci]
                dp[i+1][j | ci] %= mod

ans = sum(dp[-1])%mod
print(ans)

for i in dp:
    print(i[:10])
