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

n,*data = map(int,read().split())
it = iter(data)
dcs = [[d,c,s] for d,c,s in zip(it,it,it)]
dcs.sort()

dp = [0] * 5001
for d,c,s in dcs:
    dp2 = [0] * 5001
    for i in range(5001):
        if i < c:
            dp2[i] = dp[i]
        elif i <= d:
            dp2[i] = max(dp2[i-1], dp[i], dp[i-c] + s)
        else:
            dp2[i] = max(dp2[i-1], dp[i])
    dp,dp2 = dp2,dp

print(dp[-1])



