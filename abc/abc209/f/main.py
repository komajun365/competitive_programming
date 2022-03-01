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

n = int(n)
h = list(map(int,input().split()))
mod = 10**9 + 7

inf = 10**15
dp = [[h[0],1,0],[inf,1,0]]

for i in range(1,n):
    hi = h[i]
    dp2 = [[inf,0,0],[inf,0,0]]
    
    if dp2[0][0] > dp[0][0] + h[i-1] + h[i]:
        dp2[0] = [dp[0][0] + h[i-1] + h[i], ]

