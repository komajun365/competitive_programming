import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from collections import deque

n = int(input())
edges = [{} for i in range(n+1)]

for i in range(n-1):
    u,v,w = map(int, input().split())
    edges[u][v] = w%2
    edges[v][u] = w%2

colors = [-1]*(n+1)

d = deque()
d.append(1)
colors[1] = 0

while(len(d) > 0):
    now = d.pop()
    for key,val in edges[now].items():
        if(colors[key] == -1):
            colors[key] = (val + colors[now])%2
            d.append(key)

for i in range(1,n+1):
    print(colors[i])
