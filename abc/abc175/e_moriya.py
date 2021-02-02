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

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# pypy
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

R, C, K = map(int, readline().split())
rcv = list(map(int, read().split()))
rr = rcv[::3]
cc = rcv[1::3]
vv = rcv[2::3]
rc2v = {}
for _r, _c, _v in zip(rr, cc, vv):
    rc2v[(_r-1, _c-1)] = _v

dp = [[0]*4 for c in range(C)]

for r in range(R):
    for c in range(C):
        if(c!=0):
            dp[c][0] = max(dp[c-1][0], max(dp[c]))
        else:
            dp[c][0] = max(dp[c])

        v = 0
        if (r, c) in rc2v:
            v = rc2v[(r, c)]
        for k in range(1,4):
            if(c!=0):
                dp[c][k] = max(dp[c-1][k], dp[c-1][k-1] + v, dp[c][0] + v)
            else:
                dp[c][k] = dp[c][0] + v

print(max(dp[-1]))
for i in dp:
    print(i)
