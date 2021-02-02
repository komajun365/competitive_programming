import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
sys.setrecursionlimit(10 ** 9)

n, m = map(int,input().split())

neighbor = {}
for i in range(1,n+1):
    neighbor[i] = []

for i in range(n-1):
    x, y = map(int,input().split())
    neighbor[x].append(y)
    neighbor[y].append(x)

dp = [[-1] * (n+1) for _ in range(n+1)]

def calc_dp(x, y):
    if(dp[x][y] != -1):
        return(dp[x][y])

    if(len(neighbor[y]) == 1):
        dp[x][y] = 2 % m
        return(dp[x][y])

    temp = 1
    for i in neighbor[y]:
        if(i == x):
            continue

        temp = temp * (calc_dp(y,i)) % m

    temp = (temp + 1) % m
    dp[x][y] = temp
    return(temp)

for i in range(1,n+1):
    ans = 1
    for j in neighbor[i]:
        ans = ans * calc_dp(i,j) % m
    print(ans)
