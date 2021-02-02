import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from collections import deque

n,m = map(int,input().split())
remains = set(range(1,n+1))
edges = [[] for _ in range(n+1) ]

for i in range(m):
    x,y,z = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

ans = 0
while(len(remains) > 0):
    ans += 1

    d = deque()
    d.append(remains.pop())
    while(len(d) > 0):
        tmp = d.pop()
        for i in edges[tmp]:
            if( i in remains):
                d.append(i)
                remains.remove(i)

print(ans)
