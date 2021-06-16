# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../input.txt', 'r')
# sys.stdin = f

mod = 998244353
# 行列式 n*n行列 modは素数
def mat_det(x):
    n = len(x)
    if n == 1:
        return x[0][0] % mod

    res = 1
    pm = 0
    for i in range(n-1):
        for j in range(i,n):
            if x[i][j] != 0:
                break
        else:
            return 0
        
        if i != j:
            x[i],x[j] = x[j],x[i]
            pm += i-j
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

# import sys
# read = sys.stdin.buffer.read

# n,*a = map(int,read().split())

# mat = [[0] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         mat[i][j] = a[i*n+j]

# ans = mat_det(mat)
# print(ans)

from random import randint
import numpy as np
for _ in range(10000):
    n = randint(1,3)
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = randint(-10,10)
    
    a_np = np.array(a, dtype='int32')
    res1 = mat_det(a)
    res2 = np.linalg.det(a_np)
    res2 = round(res2) % mod
    if res1 != res2:
        print(res1,res2)
        print(a)
        print(a_np)
        exit()

    
