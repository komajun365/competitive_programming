# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

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

n = int(readline())
data = list(map(int, read().split()))
p = data[:n]
q = data[n]
it = iter(data[n+1:])
ab = [[a,b] for a,b in zip(it,it)]

root = -1
child = [set() for _ in range(n+1)]
for i,val in enumerate(p,1):
    if(val==-1):
        root = i
        child[0].add(i)
    else:
        child[val].add(i)

depth = [-1] * (n+1)
d = deque()
d.append((root,0))
while(d):
    now,dep = d.popleft()
    depth[now] = dep
    for c in child[now]:
        d.append((c,dep+1))

max_dep = max(depth)
dbl_d = (len(str(bin(max_dep))) -2)
dbl = [[-1] * (dbl_d) for _ in range(n+1)]

for j in range(1,n+1):
    dbl[j][0] = p[j-1]

dbl[0][0] = 0
dbl[root][0] = 0

for i in range(1,dbl_d):
    for j in range(n+1):
        dbl[j][i] = dbl[dbl[j][i-1]][i-1]

def get_np(now,n):
    for i in range(dbl_d):
        if(n&1):
            now = dbl[now][i]
        n = n//2
    return now

for a,b in ab:
    da = depth[a]
    db = depth[b]
    if(da<=db):
        print('No')
        continue
    if(b==get_np(a,da-db)):
        print('Yes')
    else:
        print('No')
