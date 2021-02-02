# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from heapq import heappop,heappush
sys.setrecursionlimit(10**9)
import itertools

n,m = map(int,readline().split())
a = list(map(int,readline().split()))
xy = list(map(int,read().split()))

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

def solve(n,m,a,xy):
    if(n-m==1):
        # print(0)
        # exit()
        return(0)

    uf = UnionFind(n)
    hqs = [[] for _ in range(n)]
    hq_min = []
    one_edge = []

    it = iter(xy)
    for x,y in zip(it,it):
        uf.union(x,y)

    inf = 10**10
    cnt_1 = 0
    for i in range(n):
        add = 0
        root = uf.find(i)
        if(uf.size(i) == 1):
            add = inf
            cnt_1 += 1
        heappush(hqs[root], (a[i]+add, i))

    for i in range(n):
        if(hqs[i]):
            min_i = heappop(hqs[i])
            heappush(hq_min, min_i)

    ans = 0
    while(uf.size(0) < n):
        if(len(hq_min) < 2):
            # print('Impossible')
            # exit()
            return(-1)
        i = heappop(hq_min)
        j = heappop(hq_min)
        ans += i[0]+j[0]
        i_root = uf.find(i[1])
        j_root = uf.find(j[1])
        uf.union(i[1],j[1])
        root = uf.find(i[1])
        if(root == i_root):
            child = j_root
        else:
            child = i_root
        while(hqs[child]):
            k = hqs[child].pop()
            heappush(hqs[root], k)

        if(hqs[root]):
            k = heappop(hqs[root])
            heappush(hq_min,k)

    ans -= inf * cnt_1
    # print(ans)
    return(ans)

def solve2(n,m,a,xy):
    if(n-m==1):
        return 0
    inf = 10**10
    ans = inf
    p = ((n-1)-m)*2
    if(p > n):
        return -1
    for c in itertools.permutations(range(n),p):
        xy2 = xy[::] + list(c)

        uf = UnionFind(n)
        it = iter(xy2)
        for x,y in zip(it,it):
            uf.union(x,y)

        if(uf.size(0)==n):
            tmp = 0
            for i in c:
                tmp += a[i]
            ans = min(ans,tmp)
    if(ans==inf):
        return -1
    return ans

import random
for _ in range(10000):
    n = random.randint(1,8)
    m = random.randint(0,n-1)
    a = [random.randint(1,100) for _ in range(n)]
    uf0 = UnionFind(n)
    xy = []
    for _ in range(m):
        while(True):
            x = random.randint(0,n-1)
            y = random.randint(0,n-1)
            if(not uf0.same(x,y)):
                uf0.union(x,y)
                xy = xy + [x,y]
                break

    res1 = solve(n,m,a,xy)
    res2 = solve2(n,m,a,xy)
    if(res1 != res2):
        print(n,m)
        print(a)
        print(xy)
        print(res1,res2)
        exit()












'''
１辺追加すると、頂点二つを消費する
最終的にN-1辺にしたいので、
(N-1)-M * 2 > N ならimpossible。

プリム法になればいいと思う。

18,73
48,42
3,54



'''
