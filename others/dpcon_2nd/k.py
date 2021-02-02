# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
a = list(map(int,input().split()))

dp = [0] * (k+1)
for i in range(1,k+1):
    res = 0
    for ai in a:
        if(ai > i):
            continue
        if(dp[i-ai] == 0):
            res = 1
    dp[i] = res

if(dp[-1]==1):
    print('First')
else:
    print('Second')

# print(dp)
