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

import heapq
def dijkstra(links, start, n):
    inf = 10**10
    d = [inf] * (n)
    d[start] = 0
    hq = []
    for i in links[start]:
        heapq.heappush(hq, i)
    while(hq):
        cost,i = heapq.heappop(hq)
        if( d[i] != inf):
            continue
        d[i] = cost
        for tmp in links[i]:
            cost_next, j = tmp
            if(d[j] == inf):
                heapq.heappush(hq, (cost+cost_next, j))
    return d

n,*data = list(map(int,read().split()))
it = iter(data)
xytr = []
for x,y,t,r in zip(it,it,it,it):
    xytr.append([x,y,t,r])

if(n==1):
    print(0)
    exit()

links = [[] for _ in range(n)]
for i in range(n-1):
    xi,yi,ti,ri = xytr[i]
    for j in range(i+1,n):
        xj,yj,tj,rj = xytr[j]
        dif = ((xi-xj)**2 + (yi-yj)**2)**0.5
        time = dif / min(ti,rj)
        links[i].append((time,j))
        time = dif / min(tj,ri)
        links[j].append((time,i))

d = dijkstra(links,0,n)[1:]
d.sort()

for i in range(n-1):
    d[n-2-i] += i
print(max(d))
