# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
sc = [input().split() for _ in range(m)]

inf = 10**12
dp = [[inf] * (2**n) for _ in range(m+1)]
dp[0][0] = 0
for i,(s,c) in enumerate(sc):
    c = int(c)
    s2 = 0
    for j in s:
        s2 *= 2
        s2 += (j=='Y')

    for j in range(2**n):
        dp[i+1][j] = min(dp[i][j],dp[i+1][j])
        dp[i+1][j|s2] = min(dp[i][j] + c,dp[i+1][j|s2])

ans = dp[-1][-1]
if(ans==inf):
    print(-1)
else:
    print(ans)
