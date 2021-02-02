# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f


n,m = map(int,input().split())
stones = [[] for _ in range(n)]

for i in range(n):
    a = list(map(int,input().split()))
    for j in range(a[0]):
        stones[i].append(( a[2*j+1], a[2*j+2]))

cost1 = [ [] for _ in range(n)]
cost2 = [ [] for _ in range(n)]
inf = 10**10
for i in range(1,n):
    st_from = stones[i-1]
    st_to = stones[i]
    cost1[i] = [[inf] * 10 for _ in range(10)]
    for j,st_j in enumerate(st_to):
        for k,st_k in enumerate(st_from):
            cost1[i][j][k] = (st_j[1] + st_k[1])*( abs(st_j[0] - st_k[0]) )

for i in range(2,n):
    st_from = stones[i-2]
    st_to = stones[i]
    cost2[i] = [[inf] * 10 for _ in range(10)]
    for j,st_j in enumerate(st_to):
        for k,st_k in enumerate(st_from):
            cost2[i][j][k] = (st_j[1] + st_k[1])*( abs(st_j[0] - st_k[0]) )

dp = [ [] for _ in range(n)]
for i in range(n):
    dp[i] = [[inf] * 10 for _ in range(m+1)]

dp[0][0] = [0] * 10
if(m>0):
    dp[1][1] = [0] * 10

for i in range(1,n):
    for j in range(min( (i+3)//2 , m+1 )):
        for k in range(10):
            for l in range(10):
                if(i==1)|(j==0):
                    dp[i][j][k] = min(dp[i][j][k],
                                        dp[i-1][j][l] + cost1[i][k][l])
                else:
                    dp[i][j][k] = min(dp[i][j][k],
                                        dp[i-1][j][l] + cost1[i][k][l],
                                        dp[i-2][j-1][l] + cost2[i][k][l])

ans = inf
for j in range(m+1):
    ans = min(ans, min(dp[-1][j]) )
for j in range(m):
    ans = min(ans, min(dp[-2][j]) )

print(ans)
#
# for i in dp:
#     print(i)
#
# print('###########')
#
# for i in cost2:
#     print(i)
