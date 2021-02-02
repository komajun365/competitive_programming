# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n= int(input())
gsb = [tuple(map(int,input().split())) for _ in range(2)]

def increase(num, gsb0, gsb1):
    dp = [ [num] * (num+1) for _ in range(3+1)]
    for i in range(1,4):
        w = gsb0[i-1]
        v = gsb1[i-1]
        for j in range(num+1):
            if(j < w):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-w] + v-w)

    return(dp[-1][-1])

num = increase(n,gsb[0],gsb[1])
num = increase(num,gsb[1],gsb[0])

print(num)
# print(gsb)
#
#
#
#
# [d0,g0,s0,b0]
# [d1,g1,s1,b1]
# [d2,g2,s2,b2]
# [d3,g3,s3,b3]
#
# gsb0-3 = 0
#
# d3 = g2*Ga1 + s2*Sa1 + b2*Ba1 + d2
#
# d0 = 30
# Sa1-2 = [3,5]
# Ba1-2 = [2,4]
# d3 = 45
#
# d0 = 30
# Sa1-2 = [5,3]
# Ba1-2 = [2,4]
# d3 = 100
#
# d0 = 30
# Sa1-2 = [2,4]
# Ba1-2 = [3,5]
# d3 = 45
