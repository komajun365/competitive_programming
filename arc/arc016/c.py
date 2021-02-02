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

n,m = map(int,input().split())
cost = []
prob = [dict() for _ in range(m)]
inf = 10**10

for i in range(m):
    c,cost_i = map(int,input().split())
    cost.append(cost_i)
    for j in range(c):
        id,p = map(int,input().split())
        prob[i][id-1] = p

bit_n = 2**n
dp = [0] * bit_n

for i in range(bit_n-2,-1,-1):
    min_c = inf
    for j in range(m):
        stay = 0
        ex = cost[j]
        for id,p in prob[j].items():
            if(i >> id)&1:
                stay += p
            else:
                ex += p * dp[i | (1<<id)] /100
        if(stay!=100):
            ex /= (100-stay)/100
            min_c = min(min_c , ex)

    dp[i] = min_c

print(dp[0])
