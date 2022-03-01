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

x,y,n,*th = map(int,read().split())

dp = [[0] * (x+y+1) for _ in range(x+1)]
it = iter(th)
for t,h in zip(it,it):
    for i in range(x-1,-1,-1):
        for j in range(x+y):
            if j + t > x+y:
                break
            dp[i+1][j+t] = max(dp[i+1][j+t], dp[i][j] + h)

ans = 0
for i in range(x+1):
    ans = max(ans, max(dp[i]))
print(ans)

# for i in range(x+1):
#     print(dp[i])
