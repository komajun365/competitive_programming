# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,u,v = map(int,input().split())

import sys
input = sys.stdin.readline
from collections import deque

graph = [set() for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs(graph, root):
    depth = [None] * (n+1)
    depth[0] = (-1,None)

    d = deque()
    d.append((root,0))
    max_dep = 0
    while(d):
        child,parent = d.popleft()
        depth[child] = (depth[parent][0] + 1, parent)
        if( max_dep < depth[child][0] ):
            max_dep = depth[child][0]
        for i in graph[child]:
            if i != parent:
                d.append( (i,child) )

    return depth,max_dep

depth_v,_ = bfs(graph, v)
now = list(depth_v[u])
u_depth = now[0]
limit = (u_depth+2)//2
while(now[0] > limit):
    u = now[1]
    now = depth_v[ u ]

if(len(graph[u]) == 1):
    print( depth_v[u][0]//2 )
    exit()

graph[u].discard( now[1] )
depth_new,max_dep = bfs(graph, u)
ans = limit + max_dep - 1
print(ans)
# print(limit, u, max_dep)
# print(depth_new)
