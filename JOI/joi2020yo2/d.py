# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討12分　実装11分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

# ヒープキュー（最小値・最大値の取得）
from heapq import heappop,heappush

m,r = map(int,input().split())

xy = [[0,0],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2]]
move = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        move[i][j] = abs(xy[i][0]-xy[j][0]) + abs(xy[i][1]-xy[j][1]) + 1

inf = 100
dp = [[inf] * m for _ in range(10)]

depth = [[] for _ in range(31)]
depth[0].append((0,0))
for i in range(31):
    while(depth[i]):
        rem,num1 = depth[i].pop()
        if(rem==r):
            print(i)
            exit()
        if(dp[num1][rem] != inf):
            continue
        dp[num1][rem] = i
        for j in range(10):
            rem_next = (rem*10+j)%m
            if(dp[j][rem_next] == inf):
                cost = i + move[num1][j]
                if(cost >= 31):
                    continue
                depth[cost].append((rem_next,j))


#
#
#
#         if(j%m==r):
#             print(i)
#             exit()
#         num1 = j%10
#         for k in range(10):
#              depth[i + move[num1][k] ].append(j*10+k)
#
# while(True):
#     cost,rem,num1 = heappop(hq)
#     if(rem == r):
#         print(cost)
#         break
#     if(dp[num1][rem] != inf):
#         continue
#     dp[num1][rem] = cost
#     for i in range(10):
#         rem_next = (rem*10+i)%m
#         if(dp[i][rem_next] == inf):
#             cost_next = cost + move[num1][i]
#             heappush(hq, (cost_next, rem_next,i))

# print(dp[:20])
# for i in move:
#     print(i)
#
# print(dp[9090])

'''
移動にかかるコストを求めておく。
0-3＝３みたいな。
すると、数字xを表示するのにかかる操作回数がO(|x|)で求まる。

Mで割るとRになるような数字の最小値はRである。
Rのうちもっとも操作回数が多くなるのは90909で、
5+1+(4+1)*4 = 26

大きいな・・・

x = m(100000a + b) + r
について、a=0だけ調べればいいので、0<=b<100000
これなら間に合う。
→　嘘

結局ダイクストラ

'''
