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

n,m,*data = map(int,read().split())

n2 = n+m
links = [[] for _ in range(n2)]
idx = 0
for i in range(m):
  k = data[idx]
  r = data[idx+1:idx+1+k]
  idx += 1 + k
  for rj in r:
      rj -= 1
      links[rj].append(n+i)
      links[n+i].append(rj)

dq = deque()
dq.append(0)
depth = [-1] * n2
depth[0] = 0
while dq:
    i = dq.popleft()
    for j in links[i]:
        if depth[j] != -1:
            continue
        if j < n:
            depth[j] = depth[i]+1
            dq.append(j)
        else:
            depth[j] = depth[i]
            dq.appendleft(j)

print('\n'.join(map(str,depth[:n])))

