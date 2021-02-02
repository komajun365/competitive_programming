import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())

if(n == 1):
    print(n%m)
    exit()

neighbor = {}
for i in range(1,n+1):
    neighbor[i] = []

for i in range(n-1):
    x,y = map(int, input().split())
    neighbor[x].append(y)
    neighbor[y].append(x)

dp = [{} for _ in range(n+1)]
dp_prod = [{'list':{}} for _ in range(n+1)]
prod_make_check = [0] * (n+1)
for i in range(1,n+1):
    prod_make_check[i] = -1 * len(neighbor[i])
    for idx, j in enumerate(neighbor[i]):
        dp_prod[i]['list'][j] = idx
        dp[i][j] = -1

def calc(x,y):
    if(dp[x][y] != -1):
        return(dp[x][y])

    if(len(neighbor[y]) == 1):
        dp[x][y] = 2 % m
        prod_make_check[x] += 1
        if(prod_make_check[x] == 0):
            calc_prod(x)
        return(dp[x][y])

    if(prod_make_check[y] == 0):
        idx = dp_prod[y]['list'][x]
        dp[x][y] = (1 + dp_prod[y]['left'][idx] * dp_prod[y]['right'][idx+1])  % m
        prod_make_check[x] += 1
        if(prod_make_check[x] == 0):
            calc_prod(x)
        return(dp[x][y])

    temp = 1
    for i in neighbor[y]:
        if(i == x):
            continue
        temp = temp * calc(y, i) % m
    temp = (temp+1) % m
    dp[x][y] = temp
    prod_make_check[x] += 1
    if(prod_make_check[x] == 0):
        calc_prod(x)
    return(dp[x][y])


def calc_prod(y):
    left = 1
    right = 1
    len_ = len(neighbor[y]) + 1
    dp_prod[y]['left'] = [1] * len_
    dp_prod[y]['right'] = [1] * len_
    for idx, z in enumerate(neighbor[y]):
        left = left * dp[y][z] % m
        dp_prod[y]['left'][idx+1] = left

    for idx, z in enumerate(neighbor[y][::-1]):
        right = right * dp[y][z] % m
        dp_prod[y]['right'][len_ - 2 -idx] = right

for i in range(1,n+1):
    for j in neighbor[i]:
        calc(i,j)

for i in range(1,n+1):
    print(dp_prod[i]['right'][0])
