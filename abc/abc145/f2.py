# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
h = list(map(int,input().split()))

if(n==k):
    print(0)
    exit()

inf = 10**15 * (n+1)
dp = [[inf] * (n-k+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
    for j in range(1, n-k+1):
        if(j==1):
            dp[i][j] = h[i-1]
        else:
            tmp = inf
            for l in range(1,i):
                tmp = min(tmp, dp[l][j-1] + max(0, h[i-1]- h[l-1])  )
            dp[i][j] = tmp

ans = inf
for i in range(n+1):
    ans = min(ans, dp[i][-1])

print(ans)
