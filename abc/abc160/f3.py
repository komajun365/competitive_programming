# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = 2 * 10**5 + 10
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

# 前準備
import sys
input = sys.stdin.readline
from collections import deque

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def calc(a,b):
    p_a, e_a = a
    p_b, e_b = b
    e = e_a + e_b
    p = p_a * p_b * com(e,e_a) % mod
    return(p,e)

# calc1 の定義
def calc1(c,p):
    p_num, e_num = 1,0
    for i in graph[c]:
        if i == p:
            continue
        p_num,e_num = calc((p_num, e_num) , dp1[i] )
    e_num += 1
    dp1[c] = (p_num, e_num)

# calc2 の定義
def calc2(p):
    arr = [dp1[c] if c != parent[p] else dp2[p] for c in graph[p]]

    left = [(1,0)]
    for i in arr[:-1]:
        left.append( calc(left[-1], i ) )
    right = [(1,0)]
    for i in arr[:0:-1]:
        right.append( calc(right[-1], i) )
    right = right[::-1]

    prod = []
    for a,b in zip(left,right):
        p_tmp,e_tmp = calc(a,b)
        prod.append( (p_tmp, e_tmp) )

    for c,x in zip(graph[p], prod):
        if(c != parent[p]):
            p_tmp,e_tmp = x
            dp2[c] = (p_tmp,e_tmp+1)



# 根から探索して親と探索順を記録
root = 1
order = []
parent = [0] * (n+1)
stack = deque()
stack.append(root)
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        stack.append(y)
        parent[y] = x

# 親→子の値を算出
dp1 = [None] * (n+1)
for i in order[::-1]:
    calc1(i, parent[i])

# 子→親の値を算出　累積和チックにすることでうに対策。
dp2 = [None] * (n+1)
dp2[root] = (1,0)
for i in order:
    calc2(i)

for i in range(1,n+1):
    p1,e1 = dp1[i]
    p2,e2 = dp2[i]
    e1 -= 1
    ans = calc((p1,e1), (p2,e2))[0]
    print(ans)
