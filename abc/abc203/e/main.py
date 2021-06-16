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

n,m,*data = map(int,read().split())
xy = dict()
it = iter(data)
for x,y in zip(it,it):
    if x in xy:
        xy[x].append(y)
    else:
        xy[x] = [y]

keys = list(xy.keys())
keys.sort()

point = set()
point.add(n)
for i in keys:
    add = set()
    for j in xy[i]:
        if j-1 in point or j+1 in point:
            add.add(j)
    for j in xy[i]:
        point.discard(j)
    for j in add:
        point.add(j)
print(len(point))
