# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
xy_list = [tuple(map(int,input().split())) for _ in range(n)]

links = [[] for _ in range(n+2)]
for i in range(1,m+1):
    a,b,c = map(int, input().split())
    links[a-1].append((c,b-1,i))
    links[b-1].append((c,a-1,i))

def can_go( xy_0,xy_a,xy_b ):
    x0,y0 = xy_0
    xa,ya = xy_a
    xb,yb = xy_b
    num = (xa-x0)*(xb-x0) + (ya-y0)*(yb-y0)
    return num <= 0

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

d = dijkstra(links2, 0, (m+2)*2)
ans = d[-1]//2
if(ans >= (10**10)//2):
    print(-1)
else:
    print(ans)
