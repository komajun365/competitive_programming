import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

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
        if(x == y):
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

n = int(input())
xs = []
ys = []
for i in range(n):
    x,y = map(int, input().split())
    xs.append([x,i])
    ys.append([y,i])

xs.sort()
ys.sort()

edges = []
for tmp in [xs,ys]:
    for i in range(n-1):
        tmp_0 = tmp[i]
        tmp_1 = tmp[i+1]
        edges.append([ tmp_1[0] - tmp_0[0], tmp_1[1], tmp_0[1] ])

edges.sort()

ans = 0
uf = UnionFind(n)

for edge in edges:
    cost, a, b = edge
    if uf.same(a,b) == False:
        uf.union(a,b)
        ans += cost

    if( uf.size(a) == n):
        print(ans)
        exit()
