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

n = int(readline())
c = [0] + list(map(int,read().split()))

mod = 10**9 + 7
m = 2*10**5

before = [-1] * (m+1)
dp = [0] * (n+1)
dp[0] = 1

for i,ci in enumerate(c[1:],1):
    if(c[i-1]==ci):
        dp[i] = dp[i-1]
        continue

    if(before[ci] == -1):
        dp[i] = dp[i-1]
        before[ci] = i
        continue

    dp[i] = (dp[i-1] + dp[before[ci]])%mod
    before[ci] = i

print(dp[-1])

'''
1,2,1,2,2

1,1,2,3,3

'''
