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
sys.setrecursionlimit(10**9)
from collections import defaultdict

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
        return {r: set(self.members(r)) for r in self.roots()}

n,k,l = map(int,readline().split())
pqrs = list(map(int,read().split()))
pq = pqrs[:2*k]
rs = pqrs[2*k:]

uf_l = UnionFind(n+1)
uf_t = UnionFind(n+1)

for uf,link in zip([uf_l,uf_t],[pq,rs]):
    it = iter(link)
    for a,b in zip(it,it):
        uf.union(a,b)

d = defaultdict(lambda : set())
for i in range(n+1):
    root_l = uf_l.find(i)
    root_t = uf_t.find(i)
    d[root_l * 10**6 + root_t].add(i)

ans = [0] * (n+1)
for s in d.values():
    len_s = len(s)
    for i in s:
        ans[i] = len_s

print(' '.join(map(str,ans[1:])))
