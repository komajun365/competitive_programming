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

n,m,*abc = map(int,read().split())

edge = []
for i in range(m):
    a,b,c = abc[i*3:i*3+3]
    edge.append([a-1,b-1,c,i])
edge.sort(key= lambda x: x[2])

min_cost = 0
mins = set()
uf = UnionFind(n)
links = [[] for _ in range(n)]
for a,b,c,i in edge:
    if(uf.same(a,b)):
        continue
    else:
        uf.union(a,b)
        links[a].append([c,b])
        links[b].append([c,a])
        min_cost += c
        mins.add(i)

root = 0
depth = [-1] * n
depth[root] = 0
dbl = [[] for _ in range(n)]
dbl[root].append([0,0])
stack = [root]
while(stack):
    i = stack.pop()
    for c,j in links[i]:
        if(depth[j] != -1):
            continue
        depth[j] = depth[i] + 1
        stack.append(j)
        dbl[j].append([i,c])

b_max = 18
for bi in range(1,b_max):
    for i in range(n):
        parent,max_cost = dbl[i][bi-1]
        g_parent,g_max_cost = dbl[parent][bi-1]
        dbl[i].append([g_parent, max(max_cost,g_max_cost)])

def get_max_cost(x,y):
    res = 0
    if(depth[x] < depth[y]):
        x,y = y,x
    
    dif = depth[x] - depth[y]
    for bi in range(b_max):
        if(dif >> bi)&1:
            parent,max_cost = dbl[x][bi]
            res = max(res,max_cost)
            x = parent
    
    for bi in range(b_max-1,-1,-1):
        if(dbl[x][bi][0] == dbl[y][bi][0]):
            continue
        parent,max_cost = dbl[x][bi]
        res = max(res,max_cost)
        x = parent
        parent,max_cost = dbl[y][bi]
        res = max(res,max_cost)
        y = parent

    if(x != y):
        parent,max_cost = dbl[x][0]
        res = max(res,max_cost)
        x = parent
        parent,max_cost = dbl[y][0]
        res = max(res,max_cost)
        y = parent
    
    return res

ans = [min_cost] * m
for a,b,c,i in edge:
    if(i in mins):
        continue
    max_edge = get_max_cost(a,b)
    ans[i] += c - max_edge

print('\n'.join(map(str,ans)))



'''
・最小全域木を作る
・根を決める
・親方向に向かってＬＣＡをする。
　このとき、通ったルートの中で最もコストの高い辺（コストのみでOK）を記憶しておく。

全ての辺について
・最小全域木で使っている　→　そのコストが答え
・使っていない
　LCAで祖先を求めて、一番高いコストとその辺を置き換えたときの値が答え


'''