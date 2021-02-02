# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
from collections import deque

links_rev = [set() for _ in range(n+1)]
out = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    links_rev[b].add(a)
    out[a] += 1

ends = deque()
for i in range(1,n+1):
    if(out[i] == 0):
        ends.append(i)

while(ends):
    i = ends.pop()
    for j in links_rev[i]:
        out[j] -= 1
        if(out[j]==0):
            ends.append(j)
    links_rev[i] = set()

if(sum(out) == 0):
    print(-1)
    exit()

links = [[] for _ in range(n+1)]
start = 0
for i,tmp in enumerate(links_rev):
    if(tmp):
        now = i
        for j in tmp:
            links[j].append(i)

k = 10**10
depth = [-1] * (n+1)
d = deque()

while(deque):
    if(now in done):
        break
    done.add(now)
    now = links[now][0]

done = set()
while(True):
    if(now in done):
        break
    done.add(now)
    now = links[now][0]

print(len(done))
for i in done:
    print(i)
