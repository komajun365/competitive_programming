# oj t -c "python main.py" -d "./tests/" 

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
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read

n,m,k,*data = map(int,read().split())
a = data[:n]
xy = data[n:]
mod = 10**9 + 7

mat = [[0] * n for _ in range(n)]
for i in range(n):
    mat[i][i] = 2*m

it = iter(xy)
for x,y in zip(it,it):
    x -= 1
    y -= 1
    mat[x][x] -= 1
    mat[x][y] += 1
    mat[y][x] += 1
    mat[y][y] -= 1

rev = pow(2*m, mod-2, mod)
for i in range(n):
    for j in range(n):
        mat[i][j] *= rev
        mat[i][j] %= mod

def mat_mul(x,y):
    n = len(x)
    res = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for l in range(n):
                res[i][j] += x[i][l] * y[l][j]
                res[i][j] %= mod
    
    return res

mat_ex = [mat]
for _ in range(29):
    mat_ex.append(mat_mul(mat_ex[-1], mat_ex[-1]))

mat_a = [[0] * n for _ in range(n)]
for i in range(n):
    mat_a[i][i] = 1

for i in range(30):
    if (k >> i) & 1:
        mat_a = mat_mul(mat_ex[i], mat_a)

ans = [0] * n
for i in range(n):
    for j in range(n):
        ans[i] += a[j] * mat_a[i][j]
    ans[i] %= mod

print('\n'.join(map(str,ans)))
