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
from math import gcd

n,m,k,*ab = map(int,read().split())
mod = 10**9+7

deg = [0] * n
links = [set() for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].add(b)
    links[b].add(a)
    deg[a] += 1
    deg[b] += 1

# cycle1
cyc1 = [0] * (n+1)
for i in range(1,n+1):
    for j in range(1,i+1):
        cyc1[i] += pow(k, gcd(i,j), mod)
        cyc1[i] %= mod
    cyc1[i] *= pow(i, mod-2, mod)
    cyc1[i] %= mod

# cycle2 = com(i+k-1,i)
max_n = m+k+10
fac, finv, inv = [0]*max_n, [0]*max_n, [0]*max_n

def comInit(max_n):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max_n):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max_n)

# 二項係数の計算
def com(n,k):
    if(n < k):
        return 0
    if( (n<0) | (k < 0)):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

ans = 1

# グラフから橋を削除
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    remove = True

    d = [-1] * n
    d[a] = 0
    stack = [a]
    while stack and remove:
        i = stack.pop()
        for j in links[i]:
            if i == a and j == b:
                continue
            if j == b:
                remove = False
                break
            if d[j] != -1:
                continue
            d[j] = d[i] + 1
            stack.append(j)
    
    if remove:
        deg[a] -= 1
        deg[b] -= 1
        links[a].remove(b)
        links[b].remove(a)
        ans *= k
        ans %= mod

# 橋のような点を分割する
n2 = n
for a in range(n):
    if deg[a] == 0:
        continue

    # aの隣のどの頂点と（aを通らずに）連結か調べる
    group = [-1] * n2
    stack = [a]
    while stack :
        i = stack.pop()
        if i != a and group[i] == -1:
            group[i] = i

        for j in links[i]:
            if group[j] != -1 or j == a:
                continue
            stack.append(j)
            if i != a:
                group[j] = group[i]
    
    g_dict = dict()
    for i in links[a]:
        if group[i] in g_dict:
            g_dict[group[i]].append(i)
        else:
            g_dict[group[i]] = [i]
    
    if len(g_dict) == 1:
        continue
    
    for _,val in g_dict.items():
        links.append(set())
        deg.append(0)
        for i in val:
            links[a].remove(i)
            links[i].remove(a)
            links[i].add(n2)
            links[n2].add(i)
            deg[a] -= 1
            deg[n2] += 1
        n2 += 1

# 残った連結成分が点かcycle1かcycle2か判定する
use = [0] * n2
for a in range(n2):
    if use[a] == 1:
        continue

    v_num = 0
    e_num = 0
    d = [-1] * n2
    d[a] = 0
    stack = [a]
    while stack :
        i = stack.pop()
        use[i] = 1
        v_num += 1
        e_num += deg[i]
        for j in links[i]:
            if d[j] != -1:
                continue
            d[j] = d[i] + 1
            stack.append(j)
    
    e_num //= 2
    
    if v_num == 1:
        continue

    if v_num == e_num:
        # cycle1
        ans *= cyc1[e_num]
    else:
        # cycle2
        ans *= com(k+e_num-1,k-1)
    ans %= mod

print(ans)
# print(cyc1)





