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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import sys
sys.setrecursionlimit(10**9)

class UnionFind():
    def __init__(self, n,c):
        self.n = n
        self.parents = [-1] * n
        self.cnt = [1] * n
        self.cl = [dict() for _ in range(n)] 
        for i,ci in enumerate(c):
            self.cl[i][ci] = i
        # print(self.cl)

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
            for key,val in self.cl[y_root].items():
                if( key in self.cl[x_root] ):
                    self.cnt[ self.cl[x_root][key] ] += self.cnt[ val ]
                else:
                    self.cl[x_root][key] = val
            self.parents[x_root] += self.parents[y_root]
            self.parents[y_root] = x_root
        else:
            for key,val in self.cl[x_root].items():
                if( key in self.cl[y_root] ):
                    self.cnt[ self.cl[y_root][key] ] += self.cnt[ val ]
                else:
                    self.cl[y_root][key] = val
            self.parents[y_root] += self.parents[x_root]
            self.parents[x_root] = y_root
        
        # print(self.cl)
        # print(self.cnt)

    def calc(self,x,y):
        root = self.find(x)
        if( y in self.cl[root] ):
            cap = self.cl[root][y]
            return self.cnt[cap]
        return 0

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

n,q,*data = map(int,read().split())
c = [0] + data[:n]
query = data[n:]

uf = UnionFind(n+1,c)
ans = []
it = iter(query)
for q,a,b in zip(it,it,it):
    if(q==1):
        if(not uf.same(a,b)):
            uf.union(a,b)
    else:
        ans.append(uf.calc(a,b))

print('\n'.join(map(str,ans)))

