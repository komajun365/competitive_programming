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

A,B = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[0] * (B+1) for _ in range(A+1)]

for i in range(A,-1,-1):
    for j in range(B,-1,-1):
        if i == A and j == B:
            continue
        elif i == A:
            dp[i][j] = b[j] - dp[i][j+1]
        elif j == B:
            dp[i][j] = a[i] - dp[i+1][j]
        else:
            dp[i][j] = max(b[j] - dp[i][j+1], a[i] - dp[i+1][j])

ans = (sum(a) + sum(b) + dp[0][0])//2
print(ans)