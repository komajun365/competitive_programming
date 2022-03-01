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

a,b = map(int,input().split())
x = list(map(int,input().split()))
mod = 998244353

plus = []
last = a-1
stock = 0
for xi in x[::-1]:
    if xi == 1:
        if stock > 0:
            plus.append(last)
            stock -= 1
        last -= 1
    else:
        stock += 1

dp = [0] * (b+1)
dp[0] = 1
cnt = 0
for i in range(a):
    if plus:
        if plus[-1] == i:
            cnt += 1
            plus.pop()
    for j in range(cnt,0,-1):
        dp[j] += dp[j-1]
        dp[j] %= mod

print(dp[-1])
