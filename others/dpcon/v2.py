import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
sys.setrecursionlimit(10 ** 9)

n, m = map(int,input().split())

neighbor = {}
dp = [{} for _ in range(n+1)]
dp_prod = [-1]*(n+1)
for i in range(1,n+1):
    neighbor[i] = []

for i in range(n-1):
    x, y = map(int,input().split())
    dp[x][y] = -1
    dp[y][x] = -1

def calc_dp(x, y):
    if(dp[x][y] != -1):
        return(dp[x][y])

    if(len(dp[y]) == 1):
        dp[x][y] = 2
        return(dp[x][y])

    if((dp_prod[y] != -1) & (dp[y][x] != -1)):
        dp[x][y] = 1 + dp_prod[y]//dp[y][x]
        return(dp[x][y])

    temp = 1
    for i in dp[y].keys():
        if(i == x):
            continue

        temp = temp * (calc_dp(y,i))

    if(dp[y][x] != -1):
        dp_prod[y] = temp * dp[y][x]

    dp[x][y] = temp + 1
    return(dp[x][y])

for i in range(1,n+1):
    ans = 1
    for j in dp[i].keys():
        ans = ans * calc_dp(i,j)
    print(ans % m)
