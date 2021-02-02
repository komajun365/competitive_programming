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

n = int(input())
p = list(map(int,input().split()))

# dijkstra
import heapq
def dijkstra(links, start, n, goal):
    inf = 10**5
    d = [inf] * (n)
    d[start] = 0
    hq = []
    for key,val in links[start].items():
        heapq.heappush(hq, (val,key))
    while(hq):
        cost,i = heapq.heappop(hq)
        if( d[i] != inf):
            continue
        if( i==goal ):
            return cost

        d[i] = cost
        for j,cost_next in links[i].items():
            if(d[j] == inf):
                heapq.heappush(hq, (cost+cost_next, j))
    return d

links = [{} for _ in range(1 + n**2)]
for i in range(n):
    for j in range(n):
        x = i*n+j + 1
        if(i!=0):
            links[x][x-n] = 1
        if(i!=n-1):
            links[x][x+n] = 1
        if(j!=0):
            links[x][x-1] = 1
        if(j!=n-1):
            links[x][x+1] = 1
        if(i==0)|(i==n-1)|(j==0)|(j==n-1):
            links[x][0] = 0

ans = 0
for x in p:
    ans += dijkstra(links,x,1+n**2,0)

    i = (x-1)//n
    j = (x-1)%n
    if(i!=0):
        links[x-n][x] = 0
    if(i!=n-1):
        links[x+n][x] = 0
    if(j!=0):
        links[x-1][x] = 0
    if(j!=n-1):
        links[x+1][x] = 0

print(ans)
