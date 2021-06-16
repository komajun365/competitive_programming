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

t,*case = map(int,read().split())
mod = 10**9+7

mat_e = [[0] * 16 for _ in range(16)]
mat_o = [[0] * 16 for _ in range(16)]

for i in range(16):
    for j in range(16):
        if i > j:
            mat_e[i][j] = 1
            if j >= 5:
                mat_o[i][j] = 1
        elif i == j:
            mat_e[i][j] = 1
            mat_o[i][j] = 1

def matmul(x,y):
    res = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            for k in range(16):
                res[i][j] += x[i][k] * y[k][j]
            res[i][j] %= mod
    return res

ex = []
ex.append(mat_e)
ex.append(matmul(mat_o,mat_e))

for _ in range(2,33):
    ex.append(matmul(ex[-1], ex[-1]))

def solve(n):
    if n < 5:
        return 0
    n -= 4

    mat = [[0] * 16 for _ in range(16)]
    for i in range(16):
        mat[i][i] = 1
    
    for i in range(32,-1,-1):
        if (n >> i) & 1:
            mat = matmul(ex[i],mat)
    
    return mat[-1][0]

for n in case:
    print(solve(n))

# for i in ex[2]:
#     print(i)

'''
s2-s1 = s 以下同様とする
N - (s+s1*2) - (n+n1*2) - ... = remとする

s1,n1,... を固定する（和をｘとする）と
そのケースの総和は
com(n-2x+5,10)
xの内訳が
com(x+4,4)

(n-2x+5)!(x+4)! / 10!(n-2x-5)!x!4!

x=0 のとき
(n+5)!4! / 10!(n-5)!0!4!
x=1 のとき
(n+3)!5! / 10!(n-7)!1!4!

分子の10!4!を取ると

(n-5-2x)(n-4-2x)(x+4) / (n+5-2x)(n+4-2x)(x+1)
これをかけていくことがわかる





'''