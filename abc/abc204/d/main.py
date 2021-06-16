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
t = list(map(int,input().split()))

tot = sum(t)
lim = tot//2

dp = [0] * (lim+1)
dp[0] = 1
for i in range(n):
    dp2 = [0] * (lim+1)
    ti = t[i]
    for j in range(lim+1):
        dp2[j] = dp[j]
        if j >= ti:
            if dp[j-ti] == 1:
                dp2[j] = 1
    dp,dp2 = dp2,dp

for i in range(lim,-1,-1):
    if dp[i] == 1:
        ans = tot - i
        print(ans)
        exit()