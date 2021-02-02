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
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
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

h,w = map(int,readline().split())
s = read().split()
color = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if(s[i][j] =='#'):
            color[i][j] = 1

uf = UnionFind(h*w)
for i in range(h):
    for j in range(w):
        if(j != w-1):
            if(color[i][j] != color[i][j+1]):
                uf.union(i*w+j,i*w+j+1)
        if(i != h-1):
            if(color[i][j] != color[i+1][j]):
                uf.union(i*w+j,(i+1)*w+j)

ans = 0
for gr in uf.all_group_members().values():
    even = 0
    odd = 0
    for i in gr:
        if(i%2==0):
            even += 1
        else:
            odd += 1
    ans += even*odd

print(ans)
