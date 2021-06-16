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

# pond stalkerの提出を少し修正
# https://atcoder.jp/contests/abc170/submissions/14370208

import sys
read = sys.stdin.read
from collections import deque

h,w,rs,cs,rt,ct,*s = read().split()
h,w,rs,cs,rt,ct = map(int,(h,w,rs,cs,rt,ct))
rs,cs,rt,ct = map(lambda x: x-1, (rs,cs,rt,ct))

inf = 10**7
dep = [[inf] * (w+1) for _ in range(h+1)]
for i in range(h):
    dep[i][-1] = -1
    for j in range(w):
        if s[i][j] == '#':
            dep[i][j] = -1
for j in range(w+1):
    dep[-1][j] = -1

dq = deque()
dq.append((rs,cs))
dep[rs][cs] = -1
while dq:
    x0,y0 = dq.popleft()
    d = dep[x0][y0] + 1
    for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
        x,y = x0,y0
        while True:
            x += dx
            y += dy
            if dep[x][y] < d:
                break
            elif dep[x][y] == d:
                continue
            dep[x][y] = d
            dq.append((x,y))

print(dep[rt][ct])
# for i in dep:
#     print(i)