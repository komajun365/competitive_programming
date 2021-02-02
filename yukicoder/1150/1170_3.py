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

n,a,b = map(int,input().split())
x = list(map(int,input().split()))

cango = [[0,0,0,0] for _ in range(n)]
ll,l,r,rr = 0,0,0,0
for i,xi in enumerate(x):
    while(x[ll] < xi-b):
        ll += 1
    while(x[l] <= xi-a):
        l += 1
    if(r < n):
        while(x[r] < xi+a):
            r += 1
            if(r==n):
                break
    if(rr < n):
        while(x[rr] <= xi+b):
            rr += 1
            if(rr==n):
                break
    cango[i] = [ll,l,r,rr]

uf = UnionFind(n)
for i in range(n):
    r,rr = cango[i][2:4]
    for j in range(rr-1,r-1,-1):
        if(uf.same(i,j)):
            break
        uf.union(i,j)

for i in range(n-1,-1,-1):
    ll,l = cango[i][0:2]
    for j in range(ll,l):
        if(uf.same(i,j)):
            break
        uf.union(i,j)

ans = [0] * n
for i in range(n):
    ans[i] = uf.size(i)

print('\n'.join(map(str,ans)))

for i in cango:
    print(i)
