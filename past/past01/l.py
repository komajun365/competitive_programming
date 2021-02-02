# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

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

n,m = map(int,input().split())
xyc = [list(map(int,input().split())) for _ in range(n+m)]

links = []
for i in range(n+m-1):
    xi,yi,ci = xyc[i]
    for j in range(i+1,n+m):
        xj,yj,cj = xyc[j]
        cost = ((xi-xj)**2 + (yi-yj)**2)**0.5
        if(ci!=cj):
            cost *= 10
        links.append((cost,i,j))

links.sort()

ans = 10**10
for i in range(2**m):
    cost = 0
    use = set(range(n))
    cnt = n
    for j in range(m):
        if((i>>j)&1):
            use.add(n+j)
            cnt += 1
    uf = UnionFind(n+m)
    for link in links:
        c,a,b = link
        if(not a in use)|(not b in use):
            continue
        if(uf.same(a,b)):
            continue
        uf.union(a,b)
        cost += c
        cnt -= 1
        if(cnt==1):
            break
    ans = min(ans,cost)

print(ans)
