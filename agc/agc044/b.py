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

n = int(input())
p = list(map(int,input().split()))

# 再帰関数の上限解除
import sys
sys.setrecursionlimit(10**9)

class UnionFind():
    def __init__(self, n, cost):
        self.n = n
        self.parents = [-1] * n
        self.cost = cost[::]

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

        print(x,y)

        x_root = self.find(x)
        y_root = self.find(y)
        if(x == y):
            return

        if( self.parents[x_root] <= self.parents[y_root] ):
            self.parents[x_root] += self.parents[y_root]
            self.parents[y_root] = x_root
        else:
            if(self.get_cost(x) > self.get_cost(y)):
                self.cost[y_root] = self.get_cost(x)
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

    def get_cost(self,i):
        parent = self.find(i)
        return self.cost[parent]

cnt = [0] * (n**2)
for i in range(n):
    for j in range(n):
        min_root = min(i,n-1-i,j,n-1-j)
        cnt[i*n+j] = min_root

uf = UnionFind(n**2,cnt)

ans = 0
for i in p:
    print(i)
    ans += cnt[ uf.find(i) ]
    for di in [-1,1,n,-n]:
        j = i+di
        print(j)
        print(uf.parents)
        print(uf.cost)
        if(0<=j<n**2):
            uf.union(i,j)

print(ans)
