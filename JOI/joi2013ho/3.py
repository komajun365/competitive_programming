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

import heapq
inf = 10**12
def dijkstra(links, start, n, goal):
    inf = 10**12
    d = [inf] * (n)
    d[start] = 0
    hq = []
    for cost,i in links[start]:
        heapq.heappush(hq, cost*inf + i)
    while(hq):
        num = heapq.heappop(hq)
        cost = num//inf
        i = num%inf
        if( d[i] != inf):
            continue
        d[i] = cost
        if i == goal or i == goal + n//2:
            return d
        for tmp in links[i]:
            cost_next, j = tmp
            if(d[j] == inf):
                heapq.heappush(hq, inf*(cost+cost_next)+j )
    return d

m,n,k,*xy = map(int,read().split())

rooms = dict()
lr = [[] for _ in range(n+1)]
ud = [[] for _ in range(m+1)]

for i in range(k):
    x,y = xy[i*2:i*2+2]
    rooms[x<<20 + y] = i
    lr[y].append(x)
    ud[x].append(y)

s = k
g = k+1

for x,y in [[1,1],[m,n]]:
    num = x << 20 + y
    if num in rooms:
        if x == 1:
            s = rooms[num]
        else:
            g = rooms[num]
    else:
        if x == 1:
            rooms[num] = s
        else:
            rooms[num] = g
        lr[y].append(x)
        ud[x].append(y)


k2 = k+2
links = [[] for _ in range(k2*2)]
for i in range(n+1):
    tmp = sorted(lr[i])
    l = len(tmp)
    for j in range(l-1):
        a = tmp[j]
        b = tmp[j+1]
        r1 = rooms[a << 20 + i]
        r2 = rooms[b << 20 + i]
        links[r1].append([abs(a-b),r2])
        links[r2].append([abs(a-b),r1])

for i in range(m+1):
    tmp = sorted(ud[i])
    l = len(tmp)
    for j in range(l-1):
        a = tmp[j]
        b = tmp[j+1]
        r1 = rooms[i << 20 + a] + k2
        r2 = rooms[i << 20 + b] + k2
        links[r1].append([abs(a-b),r2])
        links[r2].append([abs(a-b),r1]) 

for i in range(k):
    links[i].append([1, i+k2])
    links[i+k2].append([1, i])

d = dijkstra(links, s+k2, k2*2, g)
ans = min(d[g], d[g+k2])
if ans == inf:
    print(-1)
else:
    print(ans)
