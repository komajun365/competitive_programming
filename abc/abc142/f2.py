# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
from collections import deque

links = [set() for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    links[a].add(b)

def bfs(links, start):
    parent = [-1] * (n+1)
    selfdepth = 10**6
    d = deque()
    done = {start}
    d.append((start,0))
    while(d):
        edge,depth = d.popleft()
        for i in links[edge]:
            if(i == start):
                selfdepth = depth + 1
                parent[i] = edge
                return( selfdepth, parent )
            if(not i in done):
                parent[i] = edge
                d.append((i,depth+1))
                done.add(i)

    return ( selfdepth, parent )

k = 10**6
start = -1
for i in range(1,n+1):
    selfdepth, parent_tmp = bfs(links, i)
    if(k > selfdepth):
        k = selfdepth
        start = i
        parent_k = parent_tmp

if(start == -1):
    print(-1)
    exit()

print(k)
print(start)
now = parent_k[start]
cnt = 0
while(now != start):
    print(now)
    now = parent_k[now]
