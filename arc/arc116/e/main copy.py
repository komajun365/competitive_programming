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
from collections import deque

n,k,*uv = map(int,read().split())

links = [[] for _ in range(n)]
it = iter(uv)
for u,v in zip(it,it):
    u -= 1
    v -= 1
    links[u].append(v)
    links[v].append(u)

root = 0
dq = deque()
dq.append(root)
tp = [root]
parent = [-1] * n
parent[root] = -2

while dq:
    i = dq.popleft()
    for j in links[i]:
        if parent[j] != -1:
            continue
        parent[j] = i
        dq.append(j)
        tp.append(j)

root = tp[-1]
dq = deque()
dq.append(root)
tp = [root]
parent = [-1] * n
parent[root] = -2

while dq:
    i = dq.popleft()
    for j in links[i]:
        if parent[j] != -1:
            continue
        parent[j] = i
        dq.append(j)
        tp.append(j)

tp = tp[::-1]

def check(x):
    cnt = 0
    done = [0] * n
    for i in tp:
        if done[i] == 1:
            continue
        cnt += 1
        if cnt > k:
            return False
        p = i
        for _ in range(x):
            if parent[p] == -2:
                break
            p = parent[p]
        
        dep = dict()
        dep[p] = 0
        done[p] = 1
        stack = [p]
        while stack:
            j = stack.pop()
            for q in links[j]:
                if q in dep:
                    continue
                
                done[q] = 1
                dep[q] = dep[j] + 1
                if dep[q] != x:
                    stack.append(q)
    
    return True

ok = n
ng = 0
while ok-ng > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)

