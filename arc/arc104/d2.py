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

n,k,m = map(int,input().split())
w = n*(n-1)//2 * k
dp = [[0] * (w+1) for _ in range(n)]

dp[0][0] = 1
for i in range(1,n):
    wi = i*(i+1)//2 * k
    for j in range(wi+1):
        dp[i][j] += dp[i-1][j]
        if(j >= i):
            dp[i][j] += dp[i][j-i]
        if(j >= i*(k+1)):
            dp[i][j] -= dp[i-1][j-i*(k+1)]
        dp[i][j] %= m

ans = [-1] * (n+1)
for i in range(1,n+1):
    if(ans[n+1-i] != -1):
        ans[i] = ans[n+1-i]
    tmp = 0
    up = n-i
    down = i-1
    for j in range(w+1):
        tmp += dp[up][j] * dp[down][j]
        tmp %= m
    tmp = (tmp * (k+1) -1)%m
    ans[i] = tmp

print('\n'.join(map(str,ans[1:])))

# for i in dp:
#     print(i[:50])
