# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討20分　実装12分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import deque
import heapq

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
    hq = []
    used = set()
    used.add(start)
    c,r = cr[start*2-2:start*2]
    for i in bfs(links,start,r):
        heapq.heappush(hq, (c,i))
    cnt = 0
    while(hq):
        cost,i = heapq.heappop(hq)
        if( i in used):
            continue
        d[i] = cost
        if(i==end):
            return d[end]
        used.add(i)
        c,r = cr[i*2-2:i*2]
        for j in bfs(links,i,r):
            if(not j in used):
                heapq.heappush(hq, (cost+c, j))
        cnt += 1
    return d

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
合計エッジの数は最大でNK＝5*10**7
あとはダイクストラで計算すれば、
O(NK+NlogN)で間に合う。

と思っていたらTLE＆MLE。なぜ。
linksをすべて作るのはメモリ的にヤバそうなので、
dijkstraしながら必要に応じて作ることにする。
'''
