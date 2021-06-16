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

mod = 998244353
# 行列式 n*n行列 modは素数
def mat_det(x):
    n = len(x)
    if n == 1:
        return x[0][0]

    res = 1
    pm = 0
    for i in range(n-1):
        for j in range(i,n):
            if x[j][i] != 0:
                break
        else:
            return 0
        
        if i != j:
            x[i],x[j] = x[j],x[i]
            pm += 1
        inv = pow(x[i][i], mod-2, mod)
        res *= x[i][i]
        res %= mod
        for k in range(i,n):
            x[i][k] *= inv
            x[i][k] %= mod
        
        for j in range(i+1,n):
            mul = x[j][i]
            for k in range(i,n):
                x[j][k] -= x[i][k] * mul
                x[j][k] %= mod
    
    res *= x[-1][-1]
    if pm % 2 != 0:
        res *= -1
    res %= mod
    return res

import sys
read = sys.stdin.buffer.read

n,*a = map(int,read().split())

mat = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j] = a[i*n+j]

ans = mat_det(mat)
print(ans)