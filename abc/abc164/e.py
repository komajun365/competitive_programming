# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m,s = map(int,input().split())

uvab = [tuple(map(int,input().split())) for _ in range(m)]
cd = [tuple(map(int,input().split())) for _ in range(n)]

links = [[] for _ in range(5001 * n)]
for tmp in uvab:
    u,v,a,b = tmp
    u -= 1
    v -= 1
    for i in range(4999,0,-1):
        if(i-a >= 0):
            links[u*5001+i].append((b, v*5001+i-a))
            links[v*5001+i].append((b, u*5001+i-a))
        else:
            break
    links[u*5001+5000].append((b, v*5001+5000))
    links[v*5001+5000].append((b, u*5001+5000))

for i,tmp in enumerate(cd):
    c,d = tmp
    for j in range(5000):
        links[i*5001+j].append((d ,i*5001 + min(j+c, 5000)))

# dijkstra
import heapq
def dijkstra(links, start, n):
    inf = 10**10
    d = [inf] * (n)
    d[start] = 0
    hq = []
    used = set()
    used.add(start)
    for i in links[start]:
        heapq.heappush(hq, i)
    while(hq):
        cost,i = heapq.heappop(hq)
        if( i in used):
            continue
        d[i] = cost
        used.add(i)
        for tmp in links[i]:
            cost_next, j = tmp
            if(not j in used):
                heapq.heappush(hq, (cost+cost_next, j))
    return d

s = min(s, 5000)
d = dijkstra(links, s, 5001*n)
for i in range(1,n):
    ans = d[i*5001]
    for j in range(1,5001):
        ans = min(ans, d[i*5001+j])
    print(ans)
