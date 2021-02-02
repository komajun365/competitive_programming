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

import heapq
def dijkstra(links, start,goal, n):
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
        if i == goal:
            return d
        for tmp in links[i]:
            cost_next, j = tmp
            if(d[j] == inf):
                heapq.heappush(hq, inf*(cost+cost_next)+j )
    return d

import sys
read = sys.stdin.buffer.read

n,m,*data = map(int,read().split())
a = data[:n]
xy = data[n:]

links = [[] for _ in range(2*n+2)]
s = 2*n
g = 2*n+1

lim = max(a)
for i,ai in enumerate(a):
    links[s].append([lim-ai,i])
    links[i+n].append([ai,g])

it = iter(xy)
for x,y in zip(it,it):
    x -= 1
    y -= 1
    links[y].append([0,x+n])
    links[y+n].append([0,x+n])

d = dijkstra(links,s,g,2*n+2)

print(lim - d[g])
# print(d)