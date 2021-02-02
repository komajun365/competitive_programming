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

n = int(input())
s = []
for i in range(n):
    s.append(input())

dp = [[0,0] for _ in range(n+1)]
dp[0] = [1,1]
for i in range(1,n+1):
    if s[i-1] == 'AND':
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][0] + dp[i-1][1]*2
    else:
        dp[i][0] = dp[i-1][0]*2 + dp[i-1][1]
        dp[i][1] = dp[i-1][1]

print(dp[-1][0])