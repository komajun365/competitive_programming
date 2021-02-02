# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討9分　実装11分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**9)
import numpy as np

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
        if(x == y):
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

n,m,k = map(int,readline().split())
lines = np.array(read().split(),np.int64)
c = lines[2::3]
c_ind = np.argsort(c).tolist()

ans = [0]*m
ufs = [UnionFind(n+1) for _ in range(k+1)]
for i in c_ind[::-1]:
    a,b = lines[3*i:3*i+2]

    ok = k+1
    ng = 0
    while(ok-ng>1):
        mid = (ok+ng)//2
        if ufs[mid].same(a,b):
            ng = mid
        else:
            ok = mid

    if(ok==k+1):
        continue
    ufs[ok].union(a,b)
    ans[i] = ok

print('\n'.join(map(str,ans)))


'''
最大部分木を構築していけばよいと考えられる。

のだが、工夫せずに相続できるかどうか前から見ていくと計算量がやばい。O(NK)
新しく最もコストの高い路線を見たときに、
誰に相続させるか、効率よく知りたい。

i人目が相続できるとき、確実にi+1人目が相続できるので、
二分探索すればよい。
O(NlogK)で相続先がわかる。
これなら間に合いそう。

と思ったが、Union-Findの関数呼び出しがlog(n)なので
O(NlogNlogK)≒(3.9*10**7)
UFが経路圧縮のみだと厳しい・・・

UFを改善してrankまで見るようにした。
'''
