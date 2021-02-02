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

from decimal import *

p,n = input().split()
p = Decimal(p)
n = int(n)
one = Decimal(1)
zero = Decimal(0)

mat = [[one-p,p],[p,one-p]]

def prod(a,b):
    res = [[zero,zero],[zero,zero]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k] * b[k][j]
    return res

mat_ex = [mat]
for i in range(40):
    mat_ex.append(prod(mat_ex[-1],mat_ex[-1]))

mat_ans = [[one,zero],[zero,one]]

for i in range(40):
    if((n>>i)&1):
        mat_ans = prod(mat_ans,mat_ex[i])

ans = mat_ans[0][1]
print('{:.20f}'.format(ans))
# print('{:.10f}'.format(float('0.000000000001')))


'''

行列累乗でいいのかな？
誤差がヤバそう

とりあえずやってみよ

'''
