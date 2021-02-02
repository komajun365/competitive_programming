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

n,m,*pqc = map(int,read().split())
pq = [[] for _ in range(10**6+1)]

it = iter(pqc)
for p,q,c in zip(it,it,it):
    pq[c].append([p,q])

links = [[] for _ in range(n+1)]
new = n+1
for c_pq in pq:
    if(len(c_pq) == 0):
        continue

    points = set()
    for p,q in c_pq:
        points.add(p)
        points.add(q)

    points = list(points)
    np = len(points)
    encode = dict()
    for i,pi in enumerate(points):
        encode[pi] = i

    g = [-1] * np
    gl = [[] for _ in range(np)]
    for p,q in c_pq:
        p = encode[p]
        q = encode[q]
        gl[p].append(q)
        gl[q].append(p)

    for i in range(np):
        if(g[i] != -1):
            continue
        links.append([])
        g[i] = new
        stack=[i]
        while(stack):
            j = stack.pop()
            for k in gl[j]:
                if(g[k] != -1):
                    continue
                g[k] = new
                stack.append(k)
        new += 1

    for gi,pi in zip(g,points):
        links[gi].append(pi)
        links[pi].append(gi)

n2 = len(links)
d = [-1] * n2
d[1] = 0
stack = [1]
while(stack):
    next = []
    for i in stack:
        for j in links[i]:
            if(d[j] != -1):
                continue
            d[j] = d[i] + 1
            next.append(j)
    next,stack = stack,next

if(d[n] == -1):
    print(-1)
else:
    print(d[n]//2)
