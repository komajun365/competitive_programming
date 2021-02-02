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

import itertools
import bisect

class SegTree:
    def __init__(self, op, e, n: int = -1, v: list = []):
        assert (len(v) > 0) | (n > 0)
        if(len(v) == 0):
            v = [e()] * n
        self.__n = len(v)
        self.__log = (self.__n - 1).bit_length()
        self.__size = 1 << self.__log
        self.__d = [e()] * (2 * self.__size)
        self.__op = op
        self.__e = e
        for i in range(self.__n):
            self.__d[self.__size + i] = v[i]
        for i in range(self.__size - 1, 0, -1):
            self.__update(i)

    def __update(self, k: int):
        self.__d[k] = self.__op(self.__d[2 * k], self.__d[2 * k + 1])

    def set(self, p: int, x):
        assert (0 <= p) & (p < self.__n)
        p += self.__size
        self.__d[p] = x
        for i in range(1, self.__log + 1):
            self.__update(p >> i)

    def get(self, p: int):
        assert (0 <= p) & (p < self.__n)
        return self.__d[p + self.__size]

    def prod(self, l: int, r: int):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        sml = self.__e()
        smr = self.__e()
        l += self.__size
        r += self.__size

        while(l < r):
            if(l & 1):
                sml = self.__op(sml, self.__d[l])
                l += 1
            if(r & 1):
                r -= 1
                smr = self.__op(self.__d[r], smr)
            l //= 2
            r //= 2

        return self.__op(sml, smr)

    def all_prod(self):
        return self.__d[1]

def bellman_ford(links, start, end, n):
    inf = 10**10
    d = [inf] * (n)
    d[start] = 0
    parent = [-1] * (n)

    for _ in range(n):
        update = False
        for i in range(n):
            for j in links[i]:
                cost,neigh = j
                if(d[neigh] > d[i] + cost):
                    d[neigh] = d[i] + cost
                    parent[neigh] = i
                    update = True

        if(not update):
            # 経路の算出
            route = [end]
            now = end
            while(now != start):
                now = parent[now]
                route.append(now)

            return d,route[::-1]

    # 負の閉路がある場合（n-1回の更新で終わらない場合）
    return -1,-1

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m = map(int,readline().split())
w = list(map(int,readline().split()))
lv = list(map(int,read().split()))

max_wi = max(w)
lv2 = []
it = iter(lv)
for l,v in zip(it,it):
    lv2.append([l,v])
lv2.sort(key=lambda x:x[1])
l = [x[0] for x in lv2]
v = [x[1] for x in lv2]

min_vi = min(v)
if(max_wi > min_vi):
    print(-1)
    exit()

st = SegTree(op=max, e=lambda:0, v=l)

ans = 10**10
for p in itertools.permutations(w):
    cumsum = [0] + list(itertools.accumulate(p))
    links = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+2,n+1):
            wi = cumsum[j] - cumsum[i]
            v_ind = bisect.bisect_left(v,wi)
            if(v_ind == 0):
                cost = 0
            else:
                cost = -1 * st.prod(0,v_ind)
            links[i].append([cost,j-1])
            # print(i,j,v_ind,cost)

    dp = [0]*n
    for i in range(n-1):
        for cost,j in links[i]:
            dp[j] = min(dp[j], dp[i]+cost)

    ans = min(ans,dp[-1]*-1)
    # print(links)
    # print(cumsum)
    # print(dp)
    # break

# print(l)
# print(v)
print(ans)
