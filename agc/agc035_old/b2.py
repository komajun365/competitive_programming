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

####################
import sys
sys.setrecursionlimit(10**6)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self,x):
        if(self.parents[x] < 0):
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def size(self, x):
        return self.parents[ self.find(x) ] * -1

    def same(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        return (x_root == y_root)

    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if(x_root == y_root):
            return

        if( self.parents[x_root] <= self.parents[y_root] ):
            self.parents[x_root] += self.parents[y_root]
            self.parents[y_root] = x_root
        else:
            self.parents[y_root] += self.parents[x_root]
            self.parents[x_root] = y_root

    def members(self,x):
        root = self.find(x)
        ret = [ i for i in range(self.n) if self.find(i) == root ]
        return ret

    def roots(self):
        ret = [ i for i in range(self.n) if self.parents[i] < 0]
        return ret

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

import random

n = 10
remains = [set(range(n)) for _ in range(n)]
uf = UnionFind(n)
edges = set()
while(uf.size(0) < n):
    i = random.randint(0,n-1)
    # print(i)
    if(not remains[i]):
        continue
    js = list(remains[i])
    j = random.choice(js)
    # print(i,j)
    remains[i].remove(j)
    if(i==j):
        continue
    remains[j].remove(i)

    edges.add((i+1,j+1))
    uf.union(i,j)
    # print('add')
    # print(uf.parents)

# print(edges)
# print(len(edges))

m = len(edges)
ab = []
for i,j in edges:
    ab.append(i)
    ab.append(j)

print(ab)
print(n,m)

#####################

if(m%2==1):
    print(-1)
    exit()

it = iter(ab)
links = [[] for _ in range(n+1)]
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

for i,l in enumerate(links):
    print(i,l)

depth = [-1] * (n+1)
parent = [0] * (n+1)
child = [set() for _ in range(n+1)]
hq_dep = []
d = defaultdict(int)

stack = [1]
depth[1] = 0
heappush(hq_dep, (0,1))
now_dep = 1
while(stack):
    stack2 = []
    while(stack):
        i = stack.pop()
        for j in links[i]:
            if(depth[j] == -1):
                depth[j] = now_dep
                parent[j] = i
                d[i*10**6+j] = 1
                heappush(hq_dep,(now_dep*-1,j))
                stack2.append(j)
            else:
                child[j].add(i)
    now_dep += 1
    stack = stack2[::]

# print(parent)
# print(child)
# print(d)
# print(hq_dep)

ans = []
for _ in range(m//2):
    while(True):
        i_dep,i= hq_dep[0]
        if(parent[i]==0):
            heappop(hq_dep)
        else:
            break

    if(child[i]):
        j = child[i].pop()
        if(child[i]):
            k = child[i].pop()
        else:
            k = parent[i]
            parent[i] = 0

        if(parent[j]==i):
            parent[j] = 0
        else:
            child[j].remove(i)
        if(parent[k]==i):
            parent[k] = 0
        else:
            child[k].remove(i)

        ans.append((i,j))
        ans.append((i,k))


    else:
        j = parent[i]
        child[j].remove(i)
        heappop(hq_dep)
        if(child[j]):
            k = child[j].pop()
        else:
            k = parent[j]
            parent[j] = 0
        if(parent[k]==j):
            parent[k] = 0
        else:
            print(k,j)
            print(parent)
            print(child)
            child[k].remove(j)

        ans.append((j,i))
        ans.append((j,k))


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
