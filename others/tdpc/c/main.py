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

k,*r = map(int,read().split())
n = 2**k
dp = [1] * n

win_p = [0] * 8010
for i in range(-4000,4001):
    win_p[i] = 1 / (1 + 10**(i/400))

for i in range(k):
    dp2 = [0] * n
    for p in range(n):
        base = ((p >> i) ^ 1) << i
        for j in range(1 << i):
            q = base + j
            dp2[p] += dp[p] * dp[q] * win_p[r[q] - r[p]]
    dp,dp2 = dp2,dp

print('\n'.join(map(str,dp)))

