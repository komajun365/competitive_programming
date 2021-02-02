# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討9分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from gc import collect

h,w = map(int,readline().split())
data = read().split()

inf = 9 * 5 * 10**3 * 2
cost = [[0] * (w+2) for _ in range(h+2)]

for i in range(h):
    for j in range(w):
        s = data[i][j]
        if(s!='.'):
            cost[i+1][j+1] = int(s)

del data
collect()

dp = [[0] * (w+1) for _ in range(h+1)]
for i in range(h+1):
    for j in range(w+1):
        dp[i][j] = [inf] * 15

dp[1][1][0] = 0


for i in range(1,h+1):
    for j in range(1,w+1):
        for k in range(15):
            if(dp[i][j][k] == inf):
                continue

            # dp[i+1][j]
            if(i!=h):
                now = dp[i][j][k]
                next_k = (k>>1) & 1
                if(k>>3)==0:
                    now += cost[i+1][j]
                if(k>>2)&1:
                    dp[i+1][j][next_k+2] = min(dp[i+1][j][next_k+2], now + cost[i+1][j+1])
                    dp[i+1][j][next_k+8] = min(dp[i+1][j][next_k+8], now + cost[i+2][j])
                else:
                    dp[i+1][j][next_k+2] = min(dp[i+1][j][next_k+2], now + cost[i+1][j+1] + cost[i+1][j-1])
                    dp[i+1][j][next_k+8] = min(dp[i+1][j][next_k+8], now + cost[i+2][j] + cost[i+1][j-1])
                    dp[i+1][j][next_k+10] = min(dp[i+1][j][next_k+10], now + cost[i+1][j+1] + cost[i+2][j])
            # dp[i][j+1]
            if(j!=w):
                now = dp[i][j][k]
                next_k = (k>>1)&4
                if(k&2)==0:
                    now += cost[i][j+1]
                if(k&1):
                    dp[i][j+1][next_k+2] = min(dp[i][j+1][next_k+2], now + cost[i][j+2])
                    dp[i][j+1][next_k+8] = min(dp[i][j+1][next_k+8], now + cost[i+1][j+1])
                else:
                    dp[i][j+1][next_k+2] = min(dp[i][j+1][next_k+2], now + cost[i][j+2] + cost[i-1][j+1])
                    dp[i][j+1][next_k+8] = min(dp[i][j+1][next_k+8], now + cost[i+1][j+1] + cost[i-1][j+1])
                    dp[i][j+1][next_k+10] = min(dp[i][j+1][next_k+10], now + cost[i][j+2] + cost[i+1][j+1])

ans = min(dp[-1][-1])
print(ans)

# for i in range(h+2):
#     hoge = []
#     for j in range(w+2):
#         hoge.append(min(dp[i][j]))
#     print(hoge)
#
# print(dp[1][1])
# print(dp[1][2])
# print(dp[1][3])
# print(dp[1][4])
# print(dp[1][5])

'''
[i][j]マスについたとき、
[i-1][j+1],[i][j+1],[i+1][j-1],[i+1][j]のそれぞれのマスのお菓子を購入済みかどうかを管理しておく。
4bitで管理できる。

更新式が大変そうだけど頑張る。

'''
