# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n,m,s,t = map(int,input().split())

links_e = [[] for _ in range(n+1)]
links_s = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,a,b = map(int, input().split())
    links_e[u].append((a,v))
    links_e[v].append((a,u))
    links_s[u].append((b,v))
    links_s[v].append((b,u))

# dijkstra
import heapq
def dijkstra(links, start, n):
    inf = 10**10
    d = [inf] * (n+1)
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

d_e = dijkstra(links_e, s, n)
d_s = dijkstra(links_s, t, n)

ans = [0] * (n+1)
min_cost = 10**15
for i in range(n,0,-1):
    min_cost = min(min_cost, d_e[i]+d_s[i])
    ans[i] = min_cost

for i in range(1,n+1):
    print(10**15 - ans[i])
