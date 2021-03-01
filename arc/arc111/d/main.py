# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read
from heapq import heappop,heappush

n,m,*data = map(int,read().split())
if m==0:
    exit()

ab0 = data[:2*m]
it = iter(ab0)
ab = [[a-1,b-1] for a,b in zip(it,it)]
c = data[2*m:]

links = [dict() for _ in range(n)]
for i in range(m):
    a,b = ab[i]
    links[a][b] = [i,0]
    links[b][a] = [i,1]

ans = [''] * m
allow = {0:'->', 1:'<-'}

largest = max(c)
use = [0] * m

while largest > 0:
    for s in range(n):
        if c[s] == largest:
            break
    
    group = set()
    group.add(s)

    def dfs(i):
        for j,e in links[i].items():
            if use[e[0]] > 0:
                continue
            if j in group:
                ans[e[0]] = allow[e[1]]
                use[e[0]] = 1
                continue
            if c[j] == largest:
                ans[e[0]] = allow[e[1]]
                use[e[0]] = 1
                group.add(j)
                dfs(j)
            else:
                ans[e[0]] = allow[e[1]]
                use[e[0]] = 1
    
    dfs(s)

    for i in range(m):
        if use[i] == 1:
            a,b = ab[i]
            links[a].pop(b)
            links[b].pop(a)
            use[i] = 2
    
    for i in group:
        c[i] = 0
    
    largest = max(c)

print('\n'.join(ans))

    



