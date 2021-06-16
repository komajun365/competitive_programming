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

A,B,C = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [0] * (B+1)
dp[0] = 1/(C+1)
# print(dp)
for i in range(B):
    bi = b[i]
    for j in range(B,0,-1):
        dp[j] = dp[j] * (C+i+1-j)/(C+i+2) + dp[j-1] * (j)/(C+i+2) * bi
    dp[0] *= (C+i+1)/(C+i+2)
    # print(dp)

ans = sum(dp) * sum(a)
print(ans)
# print(sum(dp),sum(a))
