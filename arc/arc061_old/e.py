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

import sys
sys.setrecursionlimit(10**9)

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

n,m,*pqc = map(int,read().split())
pq = [[] for _ in range(10**6+1)]

it = iter(pqc)
for p,q,c in zip(it,it,it):
    pq[c].append([p,q])

links = [[] for _ in range(n+1)]
new = n+1
for c_pq in pq:
    if(len(c_pq) == 0):
        continue

    points = set()
    for p,q in c_pq:
        points.add(p)
        points.add(q)

    points = list(points)
    np = len(points)
    encode = dict()
    for i,pi in enumerate(points):
        encode[pi] = i

    uf = UnionFind(np)
    for p,q in c_pq:
        p = encode[p]
        q = encode[q]
        uf.union(p,q)

    all_group = uf.all_group_members()
    for g in all_group.values():
        links.append([])
        for gi in g:
            gi = points[gi]
            links[gi].append(new)
            links[new].append(gi)
        new += 1

n2 = len(links)
d = [-1] * n2
d[1] = 0
stack = [1]
while(stack):
    next = []
    for i in stack:
        for j in links[i]:
            if(d[j] != -1):
                continue
            d[j] = d[i] + 1
            next.append(j)
    next,stack = stack,next

if(d[n] == -1):
    print(-1)
else:
    print(d[n]//2)
