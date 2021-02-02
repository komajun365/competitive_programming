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

r,c,k = map(int,readline().split())
data = list(map(int,read().split()))
d = dict()
it = iter(data)
for ri,ci,vi in zip(it,it,it):
    d[(ri-1)*5000 + (ci-1)] = vi

dp_max = [0] * (c)

for i in range(r):
    dp = [0] * 4
    for j in range(c):
        dp[0] = max(dp[0],dp_max[j])
        if( i*5000+j  in d):
            ci = d[i*5000+j]
            for k in range(3,0,-1):
                dp[k] = max(dp[k], dp[k-1] + ci)

        dp_max[j] = max(dp)

print(dp_max[-1])
# print(d)
