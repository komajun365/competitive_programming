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
from collections import deque

n,m = map(int,readline().split())
data = list(map(int,read().split()))

links = [[] for _ in range(n+1)]
it = iter(data[:m*2])
for u,v in zip(it,it):
    links[u].append(v)
    links[v].append(u)
s = data[m*2]
k = data[m*2+1]
t = data[m*2+2:]

# t間の距離を計算
st = [-1] * (k)
links2 = [[] for _ in range(k)]
for ind,i in enumerate(t):
    d = [-1] * (n+1)
    d[i] = 0
    dq = deque()
    dq.append((i,0))
    while(dq):
        now,dif = dq.popleft()
        for j in links[now]:
            if(d[j] == -1):
                d[j] = dif + 1
                dq.append((j,dif+1))

    for ind_j,j in enumerate(t):
        if(i!=j):
            links2[ind].append((d[j],ind_j))
    st[ind] = d[s]


# dijkstra
import heapq
def dijkstra(links, st, n):
    inf = 10**10
    d = [[inf] * (1<<n) for _ in range(n)]
    hq = []
    for i,dif in enumerate(st):
        heapq.heappush(hq, (dif, (i,1<<i)))

    while(hq):
        cost,(i,bit) = heapq.heappop(hq)
        if( d[i][bit] != inf):
            continue
        if(bit == (1<<n)-1):
            print(d)
            return cost
        d[i][bit] = cost
        for tmp in links[i]:
            cost_next, j = tmp
            if((bit>>j) & 1):
                continue
            if(d[j][bit | (1<<j)] == inf):
                heapq.heappush(hq, (cost+cost_next, (j,bit | (1<<j))))
    return d

ans = dijkstra(links2,st,len(st))
print(ans)

print(st)
print(links2)
