# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# https://www.ioi-jp.org/camp/2010/2010-sp-tasks/2010-sp-day3_22.pdf

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline
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

n,m,k = map(int,input().split())
lines = [tuple(map(int,input().split())) for _ in range(m)]
lines = sorted(lines, key = lambda x: x[2])

uf = UnionFind(n)

ans = 0
tree_num = n
for line in lines:
    if(tree_num == k):
        break

    a,b,c = line
    a,b = a-1,b-1
    if(uf.same(a,b)):
        continue
    uf.union(a,b)
    ans += c
    tree_num -= 1

print(ans)


'''
方針
N個の都市を、木がK個の森にする。
最小全域木と同じようなアルゴリズムで、木がK個になったタイミングで打ち切ればOK。
その時に採用された通路のコスト合計が答え。
'''
