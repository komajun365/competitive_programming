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
    dp = [[0,0,0,0] for _ in range(4)]
    for j in range(c):
        dp[0][0] = max(dp[0][0],dp_max[j])
        if( i*5000+j  in d):
            ci = d[i*5000+j]
            #3
            if(dp[3][0] != 0):
                min_num = min(dp[3][1:4])
                if(min_num < ci):
                    dp[3][0] += ci-min_num
                    for k in range(1,4):
                        if(dp[3][k] == min_num):
                            dp[3][k] = ci
                            break
            if(dp[2][0] != 0):
                if(dp[3][0] <= dp[2][0] + ci):
                    dp[3][0] = dp[2][0] + ci
                    dp[3][1] = dp[2][1]
                    dp[3][2] = dp[2][2]
                    dp[3][3] = ci

            #2
            if(dp[1][0] != 0):
                if(dp[2][0] <= dp[1][0] + ci):
                    dp[2][0] = dp[1][0] + ci
                    dp[2][1] = dp[1][1]
                    dp[2][2] = ci
            #1
            if(dp[1][0] <= dp[0][0] + ci):
                dp[1][0] = dp[0][0] + ci
                dp[1][1] = ci
        # print(i,j)
        # print(dp)

        dp_max[j] = max(dp[0][0], dp[1][0],dp[2][0],dp[3][0])

    # print(i,j)
    # print(dp_max)

print(dp_max[-1])
# print(d)
