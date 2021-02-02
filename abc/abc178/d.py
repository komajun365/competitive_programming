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

s = int(input())
mod = 10**9 + 7
if(s < 3):
    print(0)
    exit()
elif(s < 6):
    print(1)
    exit()

dp = [1] * (s+1)
# for i in range(3,6):
#     dp[i] = 1

for i in range(6,s+1):
    for j in range(3,i-2):
        dp[i] += dp[j] * dp[i-j]
        dp[i] %= mod

print(dp[-1])
