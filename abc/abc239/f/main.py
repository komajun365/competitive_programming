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
read = sys.stdin.buffer.read

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

n,m,*data = map(int,read().split())
d = data[:n]
ab = data[n:]

if sum(d) != (n-1)*2:
    print(-1)
    exit()

uf = UnionFind(n)
it = iter(ab)
for ai,bi in zip(it,it):
    ai -= 1
    bi -= 1
    if uf.same(ai,bi):
        print(-1)
        exit()
    uf.union(ai,bi)
    d[ai] -= 1
    d[bi] -= 1

for di in d:
    if di < 0:
        print(-1)
        exit()

agm = uf.all_group_members()
l = len(agm)
rem = []
size = []
cnt = 0
for towns in agm.values():
    rem.append([])
    for i in towns:
        for _ in range(d[i]):
            rem[cnt].append(i+1)
    if len(rem[cnt]) == 0:
        print(-1)
        exit()
    size.append([len(rem[cnt]), cnt])
    cnt += 1

size.sort(reverse=True)
ans = []
rem2 = []
for i in range(l):
    si, idx = size[i]
    # print(si,idx)
    # print(rem2)
    if i == 0:
        rem2 += rem[idx]
        continue
    if len(rem2) == 0:
        print(-1)
        exit()

    if si == 1:
        x = rem2.pop()
        y = rem[idx].pop()
        ans.append('{} {}'.format(x,y))
    else:
        x = rem2.pop()
        y = rem[idx].pop()
        ans.append('{} {}'.format(x,y))
        rem2 += rem[idx]

print(*ans, sep='\n')







