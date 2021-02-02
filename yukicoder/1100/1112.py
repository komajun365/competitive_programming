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
import numpy as np

k,m,n = map(int,readline().split())
pqr = list(map(int,read().split()))
mod = 10**9+7

mat = np.zeros((36,36), dtype=np.int)
it = iter(pqr)
for p,q,r in zip(it,it,it):
    p,q,r = p-1,q-1,r-1
    mat[(p*6+q),(q*6+r)] = 1

def dot_mod(a,b):
    res = np.dot(a,b)
    res %= mod
    return res

mat_ex = [mat]
for i in range(65):
    mat_ex.append( dot_mod(mat_ex[-1],mat_ex[-1]) )

mat_n = np.zeros((36,36), dtype=np.int)
for i in range(36):
    mat_n[i,i] = 1

x = n-2
for i in range(65):
    if((x>>i)&1):
        mat_n = dot_mod(mat_n,mat_ex[i])

ans = 0
for i in range(6):
    for j in range(6):
        ans += mat_n[i][6*j]
        ans %= mod

print(ans)
# for i in range(36):
#     print(mat_n[i])
# print(mat_n)




'''
DPだけど次元増えて嫌な感じです。。。
と思ったらNがでかいので圧縮ですね。

最後の2音が(i,j)で、次の音が(j,k)になるような繊維があるかどうかを行列で表現すればよい。
6進数で表現して行列のサイズが36**2
行列の積の計算が6**6 = 46656
log(10**18)をかけても間に合いそうです。

'''
