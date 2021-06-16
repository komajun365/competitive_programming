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

n,p,*data = map(int,read().split())
ab = []
it = iter(data)
for a,b in zip(it,it):
    ab.append([a,b])

ab.sort(key=lambda x: -1 * x[0])

dp = [0] * (p+101)
for a,b in ab:
    dp2 = [0] * (p+101)
    for i in range(p+101):
        if i < a or i > p+a:
            dp2[i] = dp[i]
        else:
            dp2[i] = max(dp[i], dp[i-a] + b)
    dp,dp2 = dp2,dp
    # print(dp)

print(max(dp))