# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

n,m,s,t = map(int,input().split())

row = []
col = []
data_e = []
data_s = []
for _ in range(m):
    u,v,a,b = map(int, input().split())
    row.append(u)
    # row.append(v)
    col.append(v)
    # col.append(u)
    data_e.append(a)
    # data_e.append(a)
    data_s.append(b)
    # data_s.append(b)

graph_e = csr_matrix((data_e, (row,col)), shape=(n+1, n+1))
graph_s = csr_matrix((data_s, (row,col)), shape=(n+1, n+1))

d_e = dijkstra(csgraph=graph_e, directed=False, indices=s)
d_s = dijkstra(csgraph=graph_s, directed=False, indices=t)

ans = [0] * (n+1)
min_cost = 10**15
for i in range(n,0,-1):
    min_cost = min(min_cost, d_e[i]+d_s[i])
    ans[i] = min_cost

for i in range(1,n+1):
    print(int(10**15 - ans[i]))
