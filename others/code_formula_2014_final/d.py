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
import bisect

n = int(readline())
h = list(map(int,readline().split()))
mse = list(map(int,read().split()))

# 配るDPで考える？
it = iter(mse)
mse2 = [[m,s,e] for m,s,e in zip(it,it,it)]
mse2.sort(key=lambda x: x[1])

s = [s for m,s,e in mse2]

dp = [[0,0,-1] for _ in range(n)] #p0,p1,cnt

ans = 0
for i in range(n):
    p0_i,p1_i,cnt_i = dp[i]
    mi,_,ei = mse2[i]
    cnt += 1

    ind = bisect.bisect_left(s,ei)
    for j in range(ind,n):
        p0_j,p1_j,cnt_j = dp[j]
        mj,_,ej = mse2[j]

        if(mi != mj):
            dp[j][0] = max(p0_j, p0_i+h[0], p1_i+h[cnt])
        else:
            if(p0_i+h[0] > p1_i+h[cnt])
