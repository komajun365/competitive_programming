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
    max_num = 0
    g0,s0,b0 = gsb0
    g1,s1,b1 = gsb1
    g_max = num//g0 if (g0 < g1) else 0
    for i in range(g_max + 1):
        remain = num - i*g0
        d_g = i*g1
        s_max = remain//s0 if (s0 < s1) else 0
        for j in range( s_max + 1 ):
            remain2 = remain - j*s0
            k = remain2//b0 if (b0 < b1) else 0
            tmp = (remain2 - k*b0) + d_g + j*s1 + k*b1
            max_num = max(max_num, tmp)

    return(max_num)

num = increase(n,gsb[0],gsb[1])
num = increase(num,gsb[1],gsb[0])

print(num)

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
