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

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = i
for j in range(m+1):
    dp[0][j] = j
for i in range(1,n+1):
    for j in range(1,m+1):
        if(a[i-1] == b[j-1]):
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1]+1, dp[i-1][j]+1)
        else:
            dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)

print(dp[-1][-1])
# for i in dp:
#     print(i)