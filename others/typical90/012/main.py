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
read = sys.stdin.buffer.read

h,w,q,*query = map(int,read().split())

color = [0] * (h*w)
uf = UnionFind(h*w)
ans = []
idx = 0
for _ in range(q):
    if query[idx] == 1:
        r,c = query[idx+1:idx+3]
        r -= 1
        c -= 1
        idx += 3
        color[r*w+c] = 1
        for x,y in zip([-1,1,0,0],[0,0,-1,1]):
            x += r
            y += c
            if 0 <= x < h and 0 <= y < w:
                if color[x*w+y] == 1:
                    uf.union(r*w+c, x*w+y)
    else:
        ra,ca,rb,cb = query[idx+1:idx+5]
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        idx += 5
        if color[ra*w+ca] == 0 or color[rb*w+cb] == 0:
            ans.append('No')
        elif uf.same(ra*w+ca, rb*w+cb):
            ans.append('Yes')
        else:
            ans.append('No')

print('\n'.join(ans))

