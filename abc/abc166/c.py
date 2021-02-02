# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
h = list(map(int,input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for i in range(1,n+1):
    hi = h[i-1]
    gr = graph[i]
    tmp = 1
    for j in gr:
        hj = h[j-1]
        if(hj >= hi):
            tmp=0
    ans += tmp

print(ans)
