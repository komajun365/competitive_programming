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

# dijkstra
import heapq
def dijkstra(links, start, n):
    inf = 10**10
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
        for tmp in links[i]:
            cost_next, j = tmp
            if(d[j] == inf):
                heapq.heappush(hq, inf*(cost+cost_next)+j )
    return d

n,m,r,t,*abc = list(map(int,read().split()))
links = [[] for _ in range(n+1)]
it = iter(abc)
for a,b,c in zip(it,it,it):
    links[a].append((c,b))
    links[b].append((c,a))

ans = 0
for root in range(1,n+1):
    d = dijkstra(links, root, n+1)
    d = sorted(d[1:])
    ri = 1
    ti = 1
    while(ri < n)&(ti < n):
        if(d[ti]*r >= d[ri]*t):
            ri += 1
        else:
            ans += n-ri
            ti += 1

if(t > r):
    ans -= n * (n-1)
print(ans)
