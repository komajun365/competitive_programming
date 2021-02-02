# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討20分　実装12分 バグとり75分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import deque

def bfs(links,start,r):
    d = deque()
    d.append((start,0))
    done = set()
    done.add(start)
    while(d):
        now,depth = d.popleft()
        if(depth == r):
            break
        for j in links[now]:
            if(not j in done):
                d.append((j,depth+1))
                done.add(j)
    return done

def dijkstra(links, start, end, n):
    inf = 10**10
    d = [inf] * (n)
    d[start] = 0
    used = set()
    next = [(start,0),(0,inf)]
    for i in range(n):
        now = (0,inf)
        for j in range(1,n):
            if(not j in used)&(now[1] > d[j]):
                now = (j,d[j])
        now = now[0]
        if(now==end):
            return d[end]
        used.add(now)
        c,r = cr[now*2-2:now*2]
        for j in bfs(links, now, r):
            if(not j in used):
                d[j] = min(d[j], d[now]+c)
    return None

n,k = map(int, readline().split())
data = list(map(int,read().split()))
cr = data[:2*n]
ab = data[2*n:]

links = [[] for _ in range(n+1)]
it = iter(ab)
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

ans = dijkstra(links,1,n,n+1)
print(ans)

'''
方針
町iからタクシーに乗っていける都市をbfsで探索しておき、
コストCiで有向のエッジを張っておく。
合計エッジの数は最大でN**2＝2.5*10**7
あとはダイクストラで計算すれば、
O(NK+NlogN)で間に合う。

と思っていたらTLE＆MLE。なぜ。
自作関数だと優先度付きキューのサイズが大きくなりすぎている（maxサイズ≒エッジの総数）気がするので、
優先度付きキューを使わずに、毎回すべてのnodeを確認するダイクストラで処理する。
O(N*(N+K))のはず。

'''
