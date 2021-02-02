# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m,p = map(int,input().split())
# キュー
from collections import deque

# bellman_ford
# 負の経路がある場合は、(-1,-1)を返却する
def bellman_ford(links, start, end, n):
    inf = 10**10
    d = [inf] * (n+1)
    d[start] = 0
    parent = [-1] * (n+1)

    for _ in range(n):
        update = False
        for i in range(1,n+1):
            for j in links[i]:
                cost,neigh = j
                if(d[neigh] > d[i] + cost):
                    d[neigh] = d[i] + cost
                    parent[neigh] = i
                    update = True

        if(not update):
            # 経路の算出
            route = [end]
            now = end
            while(now != start):
                now = parent[now]
                route.append(now)

            return d,route[::-1]

    # 負の経路がある場合（n-1回の更新で終わらない場合）
    return -1,-1

abc = []
graph = [[] for _ in range(n+1)]
graph_rev = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    abc.append((a,b,p-c))
    graph[a].append(b)
    graph_rev[b].append(a)

can_go_1 = set()
can_go_n = set()

d = deque()
d.append(1)
while(d):
    tmp = d.pop()
    can_go_1.add(tmp)
    for i in graph[tmp]:
        if(not i in can_go_1):
            d.append(i)

d = deque()
d.append(n)
while(d):
    tmp = d.pop()
    can_go_n.add(tmp)
    for i in graph_rev[tmp]:
        if(not i in can_go_n):
            d.append(i)

can_go = can_go_1 & can_go_n

graph2 = [[] for _ in range(n+1)]
for tmp in abc:
    a,b,c = tmp
    if(a in can_go)&(b in can_go):
        graph2[a].append((c,b))

d , _ = bellman_ford(graph2, 1, n, n)
if(d == -1):
    print(-1)
else:
    ans = d[n] * -1
    print(max(0,ans))
