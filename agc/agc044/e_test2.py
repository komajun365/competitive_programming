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
#
# n = 3
# a = np.zeros([n+1,n+1])
# for i in range(1,n):
#     a[i][i-1] = -1
#     a[i][i] = 2
#     a[i][i+1] = -1
#
# a[0][0] = 1
# a[n][n] = 1
#
# #逆行列の計算
# inv_a = np.linalg.inv(a)
#
# print(a)
# print(inv_a)

import math

print('{:.100f}'.format(math.pi * 10**-10))
# print()
