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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m = map(int,readline().split())
a = [ sum(map(int, i.split())) for i in readlines()]

dp = [0] * 2
dp[0] = -1 * 10**15

for ai in a:
    dp[0] = max(dp[0],dp[1]+ai)
    dp[1] = max(dp[1],dp[0]-ai)

print(max(dp))
