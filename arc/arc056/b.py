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

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,s,*uv = map(int,read().split())
uf = UnionFind(n+1)
uf.union(0,s)

links = [[] for _ in range(n+1)]
it = iter(uv)
for u,v in zip(it,it):
    if(u > v):
        u,v = v,u
    links[u].append(v)

ans = []
for i in range(n,0,-1):
    for j in links[i]:
        uf.union(i,j)
    if(uf.same(0,i)):
        ans.append(i)

print('\n'.join(map(str,ans[::-1])))

'''
後ろから考える
最初は0とsだけが連結。

まず、iと周囲のスペースについて、
両方の駐車スペースが空いていれば連結する。
（Nからやるのでiより大きいものと連結すればよい）

スペースiを使いたいとき、
0番目の駐車スペースと連結なら停められる。


'''
