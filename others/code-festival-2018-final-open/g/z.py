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
# f = open('../../input.txt', 'r')
# sys.stdin = f

n = 2000
dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] += dp[i-1][j-1]
        if i - j > 0:
            dp[i][j] += dp[i-j][j]

max_num = 0
for i in dp:
    max_num = max(max_num, max(i))

print(max_num)