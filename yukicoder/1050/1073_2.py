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

import copy

n = int(input())
mod = 10**9 + 7

def mat_power(a,b):
    # aもbもm*m列の行列とする。
    m = 6
    res = [[0] *m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(m):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= mod

    return res

# x0 = [1,0,0,0,0,0]
a = [[0]*6 for _ in range(6)]
for i in range(6):
    a[0][i] = pow(6,mod-2,mod)

for i in range(5):
    a[i+1][i] = 1

a_exp = []
a_exp.append(a)
i = 1
while(2**i < 10**18):
    ai = mat_power(a_exp[-1],a_exp[-1])
    a_exp.append(copy.deepcopy(ai))
    i += 1

a_n = [[0]*6 for _ in range(6)]
for i in range(6):
    a_n[i][i] = 1

i = 0
while(n>0):
    if(n%2==1):
        a_n = mat_power(a_n,a_exp[i])
    i += 1
    n //= 2

print(a_n[0][0])
