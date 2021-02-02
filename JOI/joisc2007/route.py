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

xy_list.append(xy_list[0][::])
xy_list.append(xy_list[1][::])

links[0].append((0,n,0))
links[n].append((0,0,0))
links[1].append((0,n+1,m+1))
links[n+1].append((0,1,m+1))

def can_go( xy_0,xy_a,xy_b ):
    x0,y0 = xy_0
    xa,ya = xy_a
    xb,yb = xy_b
    num = (xa-x0)*(xb-x0) + (ya-y0)*(yb-y0)
    return num <= 0

links2 = [[] for _ in range(2*(m+2))]
for p_0, (xy_0, link) in enumerate(zip(xy_list, links)):
    len_link = len(link)
    if(len_link<=1):
        continue
    for i in range(len_link-1):
        c_a, p_a, num_a = link[i]
        xy_a = xy_list[p_a]
        for j in range(i+1,len_link):
            c_b, p_b, num_b = link[j]
            xy_b = xy_list[p_b]
            if( can_go(xy_0,xy_a,xy_b) ):
                links2[num_a*2 + (p_a < p_0)].append(( c_a+c_b , num_b*2 + (p_0 < p_b) ))
                links2[num_b*2 + (p_b < p_0)].append(( c_a+c_b , num_a*2 + (p_0 < p_a) ))

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
