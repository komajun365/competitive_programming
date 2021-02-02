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


n,x,y,*data = map(int,read().split())
mod = 10**9 + 7

max_n = n + 10
fac, finv, inv = [0]*max_n, [0]*max_n, [0]*max_n

def comInit(max_n):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max_n):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max_n)

it = iter(data)
cw = [[ci,wi] for ci,wi in zip(it,it)]

cw.sort(key= lambda x: x[1])
colors = [[] for _ in range(n+1)]

uf = UnionFind(n)
second = -1
for i in range(n):
    if cw[i][0] != cw[0][0]:
        second = i
        break

p = 0
cp,wp = cw[p]
for i in range(n):
    ci,wi = cw[i]
    colors[ci].append(i)
    if i == p:
        continue
    if ci == cp:
        continue
    if wp + wi <= y:
        uf.union(p, i)

if second != -1:
    p = second
    cp,wp = cw[p]
    for i in range(n):
        ci,wi = cw[i]
        if i == p:
            continue
        if ci == cp:
            continue
        if wp + wi <= y:
            uf.union(p, i)

for color in colors:
    if len(color) < 2:
        continue
    p = color[0]
    cp,wp = cw[p]
    for j in color[1:]:
        cj,wj = cw[j]
        if wp + wj <= x:
            uf.union(p,j)

ag = uf.all_group_members()
ans = 1

for v in ag.values():
    cnt = dict()
    for vi in v:
        if cw[vi][0] in cnt:
            cnt[cw[vi][0]] += 1
        else:
            cnt[cw[vi][0]] = 1
    
    ans *= fac[len(v)]
    ans %= mod

    for num in cnt.values():
        ans *= finv[num]
        ans %= mod

print(ans)


'''
abcd
abdc
acdb
adcb
adbc
acbd



'''