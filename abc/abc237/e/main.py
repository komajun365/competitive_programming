# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

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

import sys
read = sys.stdin.buffer.read

n,m,*data = map(int,read().split())
h = data[:n]
uv = data[n:]

links = [[] for _ in range(n)]

it = iter(uv)
for ui,vi in zip(it, it):
    ui -= 1
    vi -= 1
    if h[ui] < h[vi]:
        ui,vi = vi,ui
    links[ui].append([0 , vi])
    links[vi].append([h[ui] - h[vi] , ui])

d = dijkstra(links, 0, n)
ans = 0
for i in range(n):
    ans = max(ans, h[0] - h[i] - d[i])
print(ans)