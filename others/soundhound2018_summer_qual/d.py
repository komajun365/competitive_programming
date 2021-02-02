# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m,s,t = map(int,input().split())
uvab = [list(map(int,input().split())) for _ in range(m)]

# import
from scipy.sparse.csgraph import csgraph_from_dense,dijkstra

cost_e = [[0] * n for _ in range(n)]
cost_s = [[0] * n for _ in range(n)]

for i in uvab:
    u,v,a,b = i
    cost_e[u-1][v-1] = a
    cost_s[u-1][v-1] = b
    cost_e[v-1][u-1] = a
    cost_s[v-1][u-1] = b

csr_e = csgraph_from_dense(cost_e)
csr_s = csgraph_from_dense(cost_s)

en = dijkstra(csr_e, indices=s-1)
sn = dijkstra(csr_s, indices=t-1)


ans = [10**15] * n
min_ = int(en[n-1] + sn[n-1])
for i in range(n-1, -1, -1):
    tmp = int(en[i] + sn[i])
    min_ = min(min_, tmp)
    ans[i] -= min_

for i in ans:
    print(i)
