# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = 2*10**5 + 10
fac, finv, inv = [0]*max, [0]*max, [0]*max

def comInit(max):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max)

# 二項係数の計算
def com(n,k):
    if(n < k):
        return 0
    if( (n<0) | (k < 0)):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

####

n = int(input())
neigh = {}
degree = [0]*(n+1)

neigh[0] = {}
for i in range(1,n+1):
    neigh[i] = {0:[-1,-1]}
    neigh[0][i] = [-1,-1]

for _ in range(n-1):
    a,b = map(int, input().split())
    neigh[a][b] = [-1,-1] # 0:num 1:conb
    neigh[b][a] = [-1,-1]
    degree[a] += 1
    degree[b] += 1

def calc(parent,child):
    tmp = neigh[parent][child]
    if(tmp[0] != -1):
        return tmp[::]

    tmp_0 = neigh[0][child]
    tmp_rev = neigh[child][parent]
    if(tmp_0[0] != -1)&(tmp_rev[0] != -1):
        # print('hoge2')
        sum_n = tmp_0[0] - tmp_rev[0]
        sum_conb = tmp_0[1] * fac[tmp_rev[0]] % mod
        sum_conb = sum_conb * finv[tmp_0[0] - 1] % mod
        sum_conb = sum_conb * fac[ tmp_0[0] - 1 - tmp_rev[0]] % mod
        sum_conb = sum_conb * pow(tmp_rev[1] ,mod-2,mod) % mod

        neigh[parent][child] = [sum_n, sum_conb]
        return [sum_n, sum_conb]

    num = []
    conb = 1
    for i in neigh[child].keys():
        if(i == parent)|(i == 0):
            continue

        next = calc(child, i)
        num.append(next[0])
        conb =  conb * next[1] % mod


    if(len(num)==0):
        # print('hoge0')
        neigh[parent][child] = [1,1]
        return [1,1]

    sum_n = sum(num)
    conb_next = conb * fac[sum_n] % mod
    for i in num:
        conb_next = conb_next * finv[i] % mod

    neigh[parent][child] = [sum_n + 1, conb_next]
    if(tmp_rev[0] != -1)&(parent != 0):
        # print('hoge3 {} {}'.format(parent, child))
        sum_0 = sum_n + tmp_rev[0]
        conb_0 = fac[sum_0] * finv[sum_n] * finv[tmp_rev[0]] % mod
        conb_0 = conb_0 * conb_next * tmp_rev[1] % mod
        neigh[0][child] = [sum_0 + 1, conb_0]
        # print([sum_0 + 1, conb_0])

    # print('hoge {} {}'.format(parent, child))
    # print(neigh[parent][child][::])
    return neigh[parent][child][::]

for i in range(1,n+1):
    for j in neigh[i].keys():
        if(j != 0):
            # print('ij {} {}'.format(i,j))
            # print(calc(i,j))
            calc(i,j)
    calc(0,i)
    print(neigh[0][i][1])

# print(neigh)
