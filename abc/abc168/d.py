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

n,m = map(int,readline().split())
data = list(map(int,read().split()))
it = iter(data)

links = [[] for _ in range(n+1)]
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

d = deque()
d.append(1)
parent = [-1] * (n+1)
parent[1] = 0

while(d):
    i = d.popleft()
    for j in links[i]:
        if(parent[j] == -1):
            parent[j] = i
            d.append(j)

ans = parent[2:]
if(min(ans) == -1):
    print('No')
else:
    print('Yes')
    print('\n'.join(map(str,ans)))
