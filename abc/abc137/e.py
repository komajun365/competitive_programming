# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m,p = map(int,input().split())
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import bellman_ford, NegativeCycleError
# キュー
from collections import deque

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

data = []
row = []
col = []
for tmp in abc:
    a,b,c = tmp
    if(a in can_go)&(b in can_go):
        data.append(c)
        row.append(a)
        col.append(b)

csr_graph = csr_matrix((data, (row,col)), shape=(n+1,n+1))
try:
    bf = bellman_ford(csr_graph, indices=1)
except NegativeCycleError:
    print(-1)
    exit()

ans = int(bf[-1]) * -1
print(max(0,ans))
