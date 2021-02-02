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

l = int(input())
dp = [[0] * (l+1) for _ in range(13)]
dp[0][0] = 1
for i in range(1,13):
    for j in range(1,l+1):
        for k in range(j):
            dp[i][j] += dp[i-1][k]

print(dp[-1][-1])

    
