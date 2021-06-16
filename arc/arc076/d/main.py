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


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self,x):
        route = []
        while(x >= 0):
            route.append(x)
            x = self.parents[x]
        p = route.pop()
        for ri in route:
            self.parents[ri] = p
        return p

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
        if( self.parents[x_root] > self.parents[y_root] ):
            x_root,y_root = y_root,x_root
        self.parents[x_root] += self.parents[y_root]
        self.parents[y_root] = x_root

    def members(self,x):
        root = self.find(x)
        res = [ i for i in range(self.n) if self.find(i) == root ]
        return res

    def roots(self):
        res = [ i for i in range(self.n) if self.parents[i] < 0]
        return res

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        res = dict()
        for r in self.roots():
            res[r] = [r]
        for i in range(self.n):
            if not i in res:
                res[self.find(i)].append(i)
        return res

import sys
sys.setrecursionlimit(10**9)
read = sys.stdin.buffer.read

n,*xy = map(int, read().split())

xs = []
ys = []
for i in range(n):
    x,y = xy[i*2:i*2+2]
    xs.append((x<<20)+i)
    ys.append((y<<20)+i)
xs.sort()
ys.sort()

edges = []
for i in range(n-1):
    x1,j = divmod(xs[i], 1<<20)
    x2,k = divmod(xs[i+1], 1<<20)
    edges.append([x2-x1,j,k])
    x1,j = divmod(ys[i], 1<<20)
    x2,k = divmod(ys[i+1], 1<<20)
    edges.append([x2-x1,j,k])

edges.sort()

uf = UnionFind(n)
ans = 0
for c,i,j in edges:
    if uf.same(i,j):
        continue
    ans += c
    uf.union(i,j)
print(ans)

# print(edges)