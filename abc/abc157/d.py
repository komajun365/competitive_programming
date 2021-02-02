import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
ab = [list(map(int,input().split())) for _ in range(m)]
cd = [list(map(int,input().split())) for _ in range(k)]

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return set(i for i in range(self.n) if self.find(i) == root)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

uf = UnionFind(n+1)
for a,b in ab:
    uf.union(a,b)


f_dict = {}
b_dict = {}
for i in range(1,n+1):
    f_dict[i] = []
    b_dict[i] = []

for a,b in ab:
    f_dict[a].append(b)
    f_dict[b].append(a)

for c,d in cd:
    b_dict[c].append(d)
    b_dict[d].append(c)

ans = [0] * (n+1)

for i in range(1,n+1):
    group = uf.members(i)
    for j in b_dict[i]:
        group.discard(j)
    ans[i] = len(group) - len(f_dict[i]) - 1

print(' '.join(map(str, ans[1:])))
