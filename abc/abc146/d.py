# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline
# キュー
from collections import deque

n = int(input())
graph = [set() for _ in range(n+1)]

for i in range(1,n):
    a,b = map(int,input().split())
    graph[a].add((b,i))
    graph[b].add((a,i))

k = 0
root = 0
for i in range(1,n):
    if( k < len(graph[i]) ):
        root = i
        k = len(graph[i])

ans = [0] * (n+1)
d = deque()
d.append((root,0,0))

while(d):
    child,parent,color = d.pop()
    edges = graph[child]
    next_color = 1
    for tmp in edges:
        x,i = tmp
        if(x != parent):
            if(next_color == color):
                next_color += 1
            ans[i] = next_color
            d.append((x,child,next_color))
            next_color += 1

print(k)
for i in range(1,n):
    print(ans[i])
