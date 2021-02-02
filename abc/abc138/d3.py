import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

from collections import deque

n,q = map(int,input().split())

edge = {}
for i in range(1,n+1):
    edge[i] = []

for i in range(n-1):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

ans = [0] * (n+1)
for i in range(q):
    p,x = map(int,input().split())
    ans[p] += x

d = deque()
remains = set(range(1,n+1))
d.append(1)
remains.remove(1)

while(len(d) > 0):
    tmp = d.pop()
    for i in edge[tmp]:
        if(i in remains):
            ans[i] += ans[tmp]
            d.append(i)
            remains.remove(i)

print(' '.join(map(str, ans[1:])))
