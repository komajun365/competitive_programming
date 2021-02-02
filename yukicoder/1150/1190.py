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

n,m,p = map(int,readline().split())
s,g = map(int,readline().split())
data = list(map(int,read().split()))

from collections import deque
def dfs(links, start, n):
    inf = 10**10
    d = [inf] * (n)
    d[start] = 0
    dq = deque()
    dq.append(start)
    while(dq):
        i = dq.popleft()
        for j in links[i]:
            if(d[j] != inf):
                continue
            d[j] = d[i]+1
            dq.append(j)
    return d

links = [[] for _ in range(2*n+1)]

it = iter(data)
for u,v in zip(it,it):
    links[u].append(v+n)
    links[v].append(u+n)
    links[u+n].append(v)
    links[v+n].append(u)

ds = dfs(links,s,2*n+1)
dg = dfs(links,g,2*n+1)

ans = []
if(p%2==0):
    for i in range(1,n+1):
        if(ds[i] + dg[i] <= p)|(ds[i+n] + dg[i+n] <= p):
            ans.append(i)
else:
    for i in range(1,n+1):
        if(ds[i] + dg[i+n] <= p)|(ds[i+n] + dg[i] <= p):
            ans.append(i)

if(ans):
    print(len(ans))
    print('\n'.join(map(str,ans)))
else:
    print(-1)
