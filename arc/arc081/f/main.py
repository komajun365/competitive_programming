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
read = sys.stdin.read

h,w,*s = read().split()
h = int(h)
w = int(w)

paint = [[0] * (w-1) for _ in range(h-1)]
for i in range(h-1):
    for j in range(w-1):
        cnt = 0
        for x in [i,i+1]:
            for y in [j,j+1]:
                if s[x][y] == '.':
                    cnt += 1
        if cnt % 2 == 0:
            paint[i][j] = 1

for j in range(w-1):
    for i in range(h-3,-1,-1):
        if paint[i][j] != 0:
            paint[i][j] += paint[i+1][j]

ans = max(h,w)
for i in range(h-1):
    nums = [[] for _ in range(h)]
    for j,xj in enumerate(paint[i]):
        nums[xj].append(j)
    
    done = [0] * (w-1)
    uf = UnionFind(w-1)
    max_size = 0
    for x in range(h-1,0,-1):
        if not nums[x]:
            continue
        for j in nums[x]:
            for neigh in [-1,1]:
                neigh += j
                if neigh < 0 or neigh >= w-1:
                    continue
                if done[neigh] == 1:
                    uf.union(neigh,j)
            done[j] = 1
            max_size = max(max_size, uf.size(j))
        
        ans = max(ans, (x+1) * (max_size+1))

print(ans)



