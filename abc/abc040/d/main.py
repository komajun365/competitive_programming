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

# 再帰関数の上限解除
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
if(m==0):
    q = data[0]
    ans = [1] * q
    print('\n'.join(map(str,ans)))

aby = data[:3*m]
q = data[3*m]
vw = data[3*m+1:]
ans = [0] * q

query = []
it = iter(aby)
for a,b,y in zip(it,it,it):
    query.append([0,a,b,y])

for i in range(q):
    v,w = vw[i*2:i*2+2]
    query.append([1,i,v,w])

query.sort(key=lambda x: -1*(x[-1]*10 + x[0]))

uf = UnionFind(n+1)
for qi in query:
    if(qi[0] == 0):
        _,a,b,y = qi
        uf.union(a,b)
    else:
        _,i,v,w = qi
        ans[i] = uf.size(v)

print('\n'.join(map(str,ans)))

