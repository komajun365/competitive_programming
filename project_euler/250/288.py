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

# import numpy as np
from numba import jit,prange

p = 61
q = 10**7
mod_q = 61**10

# p = 3
# q = 10**4
# mod_q = 3**20

mod_s = 50515093

# @jit
# def calc_tn(q):
#     sn = np.zeros(q+1, dtype=np.int)
#     tn = np.zeros(q+1, dtype=np.int)
#     sn[0] = 290797
#     tn[0] = sn[0] % p
#     for i in prange(q):
#         sn[i+1] = (sn[i]**2)%mod_s
#         tn[i+1] = sn[i+1] % p
#
#     return tn

@jit
def calc_tn(p,q,mod_s):
    # sn = np.zeros(q+1, dtype=np.int)
    # tn = np.zeros(q+1, dtype=np.int)
    sn = [0] * (q+1)
    tn = [0] * (q+1)
    sn[0] = 290797
    tn[0] = sn[0] % p
    for i in prange(q):
        sn[i+1] = (sn[i]**2)%mod_s
        tn[i+1] = sn[i+1] % p

    return tn

@jit
def solve(p,q, mod_q,mod_s):
    res = 0
    tot = 0

    tn = calc_tn(p,q,mod_s)
    # for i in range(q,0,-1):
    #     tot = (tot + tn[i])%mod_q
    #     res = (res*p + tot)%mod_q

    for i in range(10):
        res += sum(tn[i+1:]) * p**(i)
        res %= mod_q

    print(res)
    # print(mod_q)
    # return res,tn

solve(p,q,mod_q,mod_s)


'''
めんどい

・階乗のpの因数
　→　割り算して足していく

・N(p,q)
でかいわー
n=qから計算していくのかな



'''
