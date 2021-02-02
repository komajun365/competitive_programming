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
readline = sys.stdin.readline
readlines = sys.stdin.readlines

h,w = map(int,readline().split())
s = read().split()
mod = 10**9 + 7

dp = [[0] * (w+2) for _ in range(h+2)]
cs_x = [[0] * (w+2) for _ in range(h+2)]
cs_y = [[0] * (w+2) for _ in range(h+2)]
cs_xy = [[0] * (w+2) for _ in range(h+2)]

dp[1][1] = 1
for i in range(1,h+1):
    for j in range(1,w+1):
        if(s[i-1][j-1] == '#'):
            continue
        if(i > 0):
            dp[i][j] += cs_x[i-1][j]
        if(j > 0):
            dp[i][j] += cs_y[i][j-1]
        if(i > 0) and (j>0):
            dp[i][j] += cs_xy[i-1][j-1]
        dp[i][j] %= mod

        if(i > 0):
            cs_x[i][j] = cs_x[i-1][j] + dp[i][j]
            cs_x[i][j] %= mod
        if(j > 0):
            cs_y[i][j] = cs_y[i][j-1] + dp[i][j]
            cs_y[i][j] %= mod
        if(i > 0) and (j>0):
            cs_xy[i][j] += cs_xy[i-1][j-1] + dp[i][j]
            cs_xy[i][j] %= mod

print(dp[-2][-2])

