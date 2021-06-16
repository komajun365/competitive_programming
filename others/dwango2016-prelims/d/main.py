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
read = sys.stdin.buffer.read

h,w,*b = map(int,read().split())

def calc(b):
    cs = [[0] * (w+1) for _ in range(h+1)]
    for i in range(h):
        for j in range(w):
            cs[i][j] = b[i*w+j] + cs[i][j-1] + cs[i-1][j] - cs[i-1][j-1]
    
    # for i in cs:
    #     print(i)

    inf = -1 * 10**10
    dp = [[inf] * (w+1) for _ in range(h+1)]
    dif = [[0] * (w+1) for _ in range(w+1)]

    for i in range(h):
        for j in range(w):
            for k in range(-1,j):
                dif[j][k] = min(dif[j][k], cs[i-1][j] - cs[i-1][k])
                dp[i][j] = max(dp[i][j], cs[i][j] - cs[i][k] - dif[j][k])
    # for i in dp:
    #     print(i)
    # for i in dif:
    #     print(i)
    
    for i in range(h):
        for j in range(1,w):
            dp[i][j] = max(dp[i][j],dp[i][j-1])
    for i in range(1,h):
        for j in range(w):
            dp[i][j] = max(dp[i][j],dp[i-1][j])
    
    return dp

dp0 = calc(b)
dp1 = calc(b[::-1])

ans = -1 * 10**10
for i in range(h):
    for j in range(w):
        if i != h-1:
            ans = max(ans, dp0[i][j] + dp1[h-i-2][-2])
            ans = max(ans, dp1[i][j] + dp0[h-i-2][-2])
        if j != w-1:
            ans = max(ans, dp0[i][j] + dp1[-2][w-j-2])
            ans = max(ans, dp1[i][j] + dp0[-2][w-j-2])
print(ans)

# for i in dp0:
#     print(i)
# for i in dp1:
#     print(i)
