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

mod = 10**9 + 7
# 行列式 n*n行列 modは素数
def mat_det(x):
    n = len(x)
    if n == 1:
        return x[0][0]

    res = 1
    pm = 0
    for i in range(n-1):
        for j in range(i,n):
            if x[j][i] != 0:
                break
        else:
            return 0
        
        if i != j:
            x[i],x[j] = x[j],x[i]
            pm += 1
        inv = pow(x[i][i], mod-2, mod)
        res *= x[i][i]
        res %= mod
        for k in range(i,n):
            x[i][k] *= inv
            x[i][k] %= mod
        
        for j in range(i+1,n):
            mul = x[j][i]
            for k in range(i,n):
                x[j][k] -= x[i][k] * mul
                x[j][k] %= mod
    
    res *= x[-1][-1]
    if pm % 2 != 0:
        res *= -1
    res %= mod
    return res


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

n,m,*abc = map(int,read().split())
base = 1<<20

edge = [[] for _ in range(10**5+1)]
it = iter(abc)
for a,b,c in zip(it,it,it):
    a -= 1
    b -= 1
    edge[c].append((a<<20) + b)

uf = UnionFind(n)
cost = 0
cnt = 1
for ci in range(1,10**5+1):
    cand = []
    ver = set()
    for ab in edge[ci]:
        a,b = divmod(ab, base)
        a = uf.find(a)
        b = uf.find(b)
        if a == b:
            continue
        ver.add(a)
        ver.add(b)
        cand.append([a,b])
    
    if len(ver) == 0:
        continue
    
    encode = dict()
    for i,vi in enumerate(ver):
        encode[vi] = i
    
    links = [[] for _ in range(len(ver))]
    for a,b in cand:
        a = encode[a]
        b = encode[b]
        links[a].append(b)
        links[b].append(a)
    
    use = [0] * len(ver)
    for i in range(len(ver)):
        if use[i] == 1:
            continue
        connect = set()
        connect.add(i)
        stack = [i]
        use[i] = 1
        while stack:
            j = stack.pop()
            for k in links[j]:
                if use[k] == 1:
                    continue
                stack.append(k)
                connect.add(k)
                use[k] = 1
        
        encode2 = dict()
        for j,cj in enumerate(connect):
            encode2[cj] = j
        
        ml = len(connect) - 1
        mat = [[0] * ml for _ in range(ml)]
        for cj in connect:
            j = encode2[cj]
            for ck in links[cj]:
                k = encode2[ck]
                if j == ml:
                    pass
                elif k == ml:
                    mat[j][j] += 1
                else:
                    mat[j][j] += 1
                    mat[j][k] -= 1
    
        cnt *= mat_det(mat)
        cnt %= mod

    for a,b in cand:
        a = uf.find(a)
        b = uf.find(b)
        if a == b:
            continue
        uf.union(a,b)
        cost += ci

print(cost, cnt)

    
