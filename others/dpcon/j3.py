import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import numpy as np

n = int(input())
a = input().split()

c1 = a.count('1')
c2 = a.count('2')
c3 = a.count('3')

# dp =[ [[-1] * (n+1) for _ in range(n+1)] for __ in range(c3+1)]
# dp = np.full((c3+1, c2+c3+1, n+1), -1.0)
# dp[0][0][0] = 0

from functools import lru_cache
@lru_cache(maxsize=None)
def calc_dp(t3,t2,t1):
    # global dp
    # if(dp[t3][t2][t1] > -1):
    #     return dp[t3][t2][t1]
    if(t3+t2+t1==0):
        return 0

    temp = 0
    if(t3 > 0):
        temp += calc_dp(t3-1,t2+1,t1) * t3/(t1+t2+t3)
    if(t2 > 0):
        temp += calc_dp(t3,t2-1,t1+1) * t2/(t1+t2+t3)
    if(t1 > 0):
        temp += calc_dp(t3,t2,t1-1) * t1/(t1+t2+t3)
    temp = temp + n/(t1+t2+t3)

    # dp[t3][t2][t1] = temp
    return temp

print(calc_dp(c3,c2,c1))
