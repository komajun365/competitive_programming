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
import bisect
from collections import deque

h,w,n,sx,sy,gx,gy,*xy = map(int,read().split())

rock_x = dict()
rock_y = dict()
it = iter(xy)
for xi,yi in zip(it,it):
    if yi in rock_x:
        rock_x[yi].append(xi)
    else:
        rock_x[yi] = [xi]
    if xi in rock_y:
        rock_y[xi].append(yi)
    else:
        rock_y[xi] = [yi]

for k in rock_x.keys():
    rock_x[k].sort()
for k in rock_y.keys():
    rock_y[k].sort()

d = dict()
s = (sx << 30) + sy
mask = (1<<30) -1
d[s] = 0
stack = deque()
stack.append(s)
while stack:
    a = stack.popleft()
    sx = a >> 30
    sy = a & mask
    if sy in rock_x:
        v = rock_x[sy]
        idx = bisect.bisect_right(v, sx)
        if idx != 0:
            b = ((v[idx-1] + 1) << 30) + sy
            if b not in d:
                d[b] = d[a] + 1
                stack.append(b)
        if idx != len(v):
            b = ((v[idx] - 1) << 30) + sy
            if b not in d:
                d[b] = d[a] + 1
                stack.append(b)

    if sx in rock_y:
        v = rock_y[sx]
        idx = bisect.bisect_right(v, sy)
        if idx != 0:
            b = (sx << 30) + (v[idx-1]+1)
            if b not in d:
                d[b] = d[a] + 1
                stack.append(b)
        if idx != len(v):
            b = (sx << 30) + (v[idx]-1)
            if b not in d:
                d[b] = d[a] + 1
                stack.append(b)


g = (gx << 30) + gy
if g in d:
    print(d[g])
else:
    print(-1)

# for k,v in d.items():
#     print(k>>30, k & ((1<<30)-1), v)

# print('==')

# for k,v in links.items():
#     for vi in v:
#         print(k>>30, k & ((1<<30)-1), vi>>30, vi & ((1<<30)-1))





# links = dict()
# for k,v in rock_x.items():
#     lv = len(v)
#     print(k,v)
#     for i in range(lv-1):
#         a = ((v[i]+1) << 30) + (k)
#         b = ((v[i+1]-1) << 30) + (k)
#         point.add(a)
#         point.add(b)
#         if a in links:
#             links[a].append(b)
#         else:
#             links[a] = [b]
#         if b in links:
#             links[b].append(a)
#         else:
#             links[b] = a

# for k,v in rock_y.items():
#     lv = len(v)
#     for i in range(lv-1):
#         a = (v[i]+1) + (k << 30)
#         b = (v[i+1]-1) + (k << 30)
#         point.add(a)
#         point.add(b)
#         if a in links:
#             links[a].append(b)
#         else:
#             links[a] = [b]
#         if b in links:
#             links[b].append(a)
#         else:
#             links[b] = a