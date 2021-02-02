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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,*data = map(int,read().split())
ab_0 = data[:2*m]
q = data[2*m]
xyz_0 = data[2*m+1:]

xyz = []
it = iter(xyz_0)
for x,y,z in zip(it,it,it):
    xyz.append([x,y,z])

ab = []
decode = []
uf = UnionFind(n+1)
for i in range(m):
    a,b = ab_0[i*2:i*2+2]
    if(not uf.same(a,b)):
        uf.union(a,b)
        ab.append([a,b])
        decode.append(i)

ans = [-1] * q
oks = [n-1] * q
ngs = [-1] * q

mids = [[] for _ in range(n-1)]
mids[(n-2)//2] = list(range(q))

done = 0
while(done < q):
    uf = UnionFind(n+1)
    for i in range(n-1):
        a,b = ab[i]
        uf.union(a,b)

        while(mids[i]):
            j = mids[i].pop()
            x,y,z = xyz[j]
            if(uf.same(x,y)):
                num = uf.size(x)
            else:
                num = uf.size(x) + uf.size(y)
            if(num < z):
                ngs[j] = i
            else:
                oks[j] = i
            if(oks[j] - ngs[j] == 1):
                ans[j] = decode[oks[j]] + 1
                done += 1
            else:
                mids[(oks[j] + ngs[j])//2].append(j)

print('\n'.join(map(str,ans)))


