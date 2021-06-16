# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import deque

n,m,t = map(int,readline().split())
a = list(map(int,readline().split()))

if(t==0):
    print(sum(a))
    exit()

if(m==0):
    print(0)
    exit()

uv = list(map(int,read().split()))
links = [[] for _ in range(n*2+1)]

it = iter(uv)
for u,v in zip(it,it):
    links[u].append(v+n)
    links[v].append(u+n)
    links[u+n].append(v)
    links[v+n].append(u)

for i,ai in enumerate(a,1):
    if(ai==1)&(len(links[i])> 0):
        links[0].append(i)

inf = 10**9
d = [inf] * (2*n+1)
d[0] = 0
deq = deque()
deq.appendleft(0)
while(deq):
    i = deq.popleft()
    for j in links[i]:
        if(d[j] != inf):
            continue
        d[j] = d[i] + 1
        deq.append(j)

t += 1
ans = 0
if(t%2 == 0):
    for di in d[n+1:]:
        if(di <= t):
            ans += 1
else:
    for di in d[1:n+1]:
        if(di <= t):
            ans += 1

print(ans)
