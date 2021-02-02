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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,x,*data = map(int,read().split())
mod = 10**9+7

it = iter(data)
uvw = [[u-1,v-1,w] for u,v,w in zip(it,it,it)]
uvw.sort(key=lambda x: x[2])

if(n<=2):
    print(0)
    exit()

costs = [-1]
under_x = [0]
over_x = [0]
for z in range(1,m):
    uf = UnionFind(n)
    uz,vz,w = uvw[z]
    uf.union(uz,vz)
    cost = w
    for i in range(m):
        if(i == z):
            continue
        u,v,w = uvw[i]
        if not uf.same(u,v):     
            uf.union(u,v)
            cost += w
    
    costs.append(cost)
    under_x.append(under_x[-1] + (cost<x))
    over_x.append(over_x[-1] + (cost>x))

ans = 0
for i in range(1,m):
    if(costs[i] == x):
        ans += pow(2, m-i-1 - (under_x[-1] - under_x[i]) + over_x[i-1], mod)
        ans %= mod

ans *= 2
ans %= mod
# print(ans)
# print(costs)
# print(under_x)

# 102行目以降、これでもOK
# costs.sort()
# ans = 0
# for i,ci in enumerate(costs):
#     if(ci == x):
#         ans += pow(2, m-i,mod)
# ans %= mod
# print(ans)

