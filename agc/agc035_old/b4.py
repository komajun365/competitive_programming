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
from heapq import heappop,heappush
from collections import defaultdict

n,m = map(int,readline().split())
ab = list(map(int,read().split()))

if(m%2==1):
    print(-1)
    exit()

it = iter(ab)
links = [[] for _ in range(n+1)]
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

depth = [-1] * (n+1)
parent = [0] * (n+1)
child = [set() for _ in range(n+1)]
hq_dep = []

stack = [1]
depth[1] = 0
# heappush(hq_dep, (0,1))
now_dep = 1
while(stack):
    stack2 = []
    while(stack):
        i = stack.pop()
        for j in links[i]:
            if(depth[j] == -1):
                depth[j] = now_dep
                parent[j] = i
                heappush(hq_dep,(now_dep*-1,j))
                stack2.append(j)
            else:
                child[j].add(i)
    now_dep += 1
    stack = stack2[::]

# 0:未定　1:done
ans = []
d = defaultdict(int)
outs = [0] * (n+1)
while(hq_dep):
    i_dep,i = heappop(hq_dep)
    for j in child[i]:
        if(d[min(i,j)*10**6 + max(i,j)] == 0):
            d[min(i,j)*10**6 + max(i,j)] = 1
            outs[j] += 1
            ans.append([j,i])
    j = parent[i]
    if(outs[i]%2==1):
        d[min(i,j)*10**6 + max(i,j)] = 1
        outs[i] += 1
        ans.append([i,j])
    else:
        d[min(i,j)*10**6 + max(i,j)] = 1
        outs[j] += 1
        ans.append([j,i])

print('\n'.join(map(lambda x: ' '.join(map(str,x)), ans)))





'''
端点から決めていけば確定する？

閉路どうしよう問題
K5とか。

先に閉路？

偶数長の道は処理できる。

二部グラフである必要ある？
→　ない


一本出たら、もう一本出さないといけない。

2辺消して、継続できればOK？

頂点数奇数の木はいける


木がいけるのにグラフがいけないことある？
→　全体の連結を保ったまま辺を除いていければよい

根を決めておいて、一番遠いところから処理すればよい？

頂点深さのheapqを持つ
一番深い頂点をとる。
端点じゃなければ、2辺取る。

端点なら1辺とって、行った先か一番深いところへ行く

これを繰り返せばOKでは？

'''
