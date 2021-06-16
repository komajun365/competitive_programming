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

k = int(input())
mod = 10**9 + 7

if k%9 != 0:
    print(0)
    exit()

dp = [0] * (k+20)
dp[0] = 1

tot = 0
for i in range(1,k+1):
    tot += dp[i-1] - dp[i-10]
    tot %= mod
    dp[i] = tot
print(dp[k])

