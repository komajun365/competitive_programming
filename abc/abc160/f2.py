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

# キュー
from collections import deque

remains = set(range(1,n+1))
stack = deque()
stack2 = deque()
tmp = -1
while(len(remains) > 0):
    for i in remains:
        if(degree[i] == 1):
            tmp = i
            break
    remains.remove(i)

    for i in neigh[i].keys():
        if(i in remains):
            stack.appendleft([i, tmp])
            stack2.append([tmp, i])
            degree[i] -= 1
            degree[tmp] -= 1
            break

while(len(stack2) > 0):
    i,j = stack2.pop()
    stack.appendleft([i,j])

for i in range(1,n+1):
    stack.appendleft([0,i])

while(len(stack) > 0):
    parent, child = stack.pop()
    tmp = neigh[parent][child]
    if(tmp[0] != -1):
        continue

    tmp_0 = neigh[0][child]
    tmp_rev = neigh[child][parent]
    if(tmp_0[0] != -1)&(tmp_rev[0] != -1):
        sum_n = tmp_0[0] - tmp_rev[0]
        sum_conb = tmp_0[1] * fac[tmp_rev[0]] % mod
        sum_conb = sum_conb * finv[tmp_0[0] - 1] % mod
        sum_conb = sum_conb * fac[ tmp_0[0] - 1 - tmp_rev[0]] % mod
        sum_conb = sum_conb * pow(tmp_rev[1] ,mod-2,mod) % mod

        neigh[parent][child] = [sum_n, sum_conb]
        continue

    num = []
    conb = 1
    for j in neigh[child].keys():
        if(j == parent)|(j == 0):
            continue

        next = neigh[child][j]
        num.append(next[0])
        conb =  conb * next[1] % mod

    if(len(num)==0):
        neigh[parent][child] = [1,1]
        continue

    sum_n = sum(num)
    conb_next = conb * fac[sum_n] % mod
    for j in num:
        conb_next = conb_next * finv[j] % mod

    neigh[parent][child] = [sum_n + 1, conb_next]
    if(tmp_rev[0] != -1)&(parent != 0):
        sum_0 = sum_n + tmp_rev[0]
        conb_0 = fac[sum_0] * finv[sum_n] * finv[tmp_rev[0]] % mod
        conb_0 = conb_0 * conb_next * tmp_rev[1] % mod
        neigh[0][child] = [sum_0 + 1, conb_0]

for i in range(1,n+1):
    print(neigh[0][i][1])
