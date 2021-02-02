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
from numba import njit,prange
import numpy as np

n,m = map(int,readline().split())
a = list(map(int,readline().split()))
a += [0,0,0]
b = list(map(int,read().split()))
imos = np.zeros((n+2,n+2),dtype=('int'))

@njit(parallel=True)
def solve(n,m,a,b,imos):
    for i in range(m):
        left = list(range(-1,n+1))
        right = list(range(1,n+3))

        bi = [(val,j) for j,val in enumerate(b[i::m], 1)]
        bi.sort()
        for val,j in bi:
            l = left[j]
            r = right[j]
            imos[l+1,j] += val
            imos[l+1,r] -= val
            imos[j+1,j] -= val
            imos[j+1,r] += val
            right[l] = r
            left[r] = l

    for i in prange(n+1):
        for j in range(1,n+1):
            imos[i,j] += imos[i,j-1]

    for i in range(1,n+1):
        for j in prange(n+1):
            imos[i,j] += imos[i-1,j]

    ans = 0
    for i in range(1,n+1):
        dif = 0
        for j in range(i,n+1):
            ans = max(ans,imos[i,j] - dif)
            dif += a[j-1]

    print(int(ans))

solve(n,m,a,b,imos)





'''
i~jの焼き肉店に行くときのおいしさの最大値が知りたい




'''
