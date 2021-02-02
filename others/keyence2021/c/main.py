# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.read

H,W,K,*hwc = read().split()
H = int(H)
W = int(W)
K = int(K)
mod = 998244353

d = {'R':1,'D':2,'X':3}
lit = [[0] * W for _ in range(H)]
imos_i = [[1] * (W+1) for _ in range(H+1)]
imos_j = [[1] * (W+1) for _ in range(H+1)]

it = iter(hwc)
for h,w,c in zip(it,it,it):
    h = int(h) - 1
    w = int(w) - 1
    lit[h][w] = d[c]
    imos_i[h][w] = 0
    imos_j[h][w] = 0

for i in range(H):
    imos_i[i][-1] = 0
    imos_j[i][-1] = 0

for j in range(W):
    imos_i[-1][j] = 0
    imos_j[-1][j] = 0

for i in range(H):
    for j in range(W-1)[::-1]:
        imos_i[i][j] += imos_i[i][j+1]

for j in range(W):
    for i in range(H-1)[::-1]:
        imos_j[i][j] += imos_j[i+1][j]

ex3 = [1] * 5001
for i in range(5000):
    ex3[i+1] = ex3[i] * 3
    ex3[i+1] %= mod

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i == H-1 and j == W-1:
            continue
        if i != H-1:
            if lit[i][j] == 2 or lit[i][j] == 3:
                dp[i+1][j] += (dp[i][j] * ex3[imos_i[i][j+1]]) % mod
            elif lit[i][j] == 0:
                dp[i+1][j] += (dp[i][j] * 2 * ex3[imos_i[i][j+1]]) % mod
            dp[i+1][j] %= mod
        if j != W-1:
            if lit[i][j] == 1 or lit[i][j] == 3:
                dp[i][j+1] += (dp[i][j] * ex3[imos_j[i+1][j]]) % mod
            elif lit[i][j] == 0:
                dp[i][j+1] += (dp[i][j] * 2 * ex3[imos_j[i+1][j]]) % mod
            dp[i][j+1] %= mod

if lit[-1][-1] == 0:
    dp[-1][-1] *= 3
    dp[-1][-1] %= mod

print(dp[-1][-1])

# print(imos_i)
# print(imos_j)
# print(dp)