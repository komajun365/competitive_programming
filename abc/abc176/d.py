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
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from heapq import heappop,heappush

h,w = map(int,readline().split())
ch,cw = map(int,readline().split())
dh,dw = map(int,readline().split())
s = read().split()

ch -= 1
cw -= 1
dh -= 1
dw -= 1

wall = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if(s[i][j] == '#'):
            wall[i][j] = 1

cost = [[-1] * w for _ in range(h)]
hq = [(ch,cw,0)]

while(hq):
    xi,yi,ci = heappop(hq)
    if(cost[xi][yi] != -1):
        continue
    cost[xi][yi] = ci

    for dx in range(-2,3):
        for dy in range(-2,3):
            xj,yj = xi+dx,yi+dy
            # print(xi,yi,xj,yj)
            if(xj<0)|(xj>=h)|(yj<0)|(yj>=w):
                continue
            if(cost[xj][yj]!=-1):
                continue
            if(xi==xj)&(yi==yj):
                continue
            if(wall[xj][yj]==1):
                continue
            if(abs(xi-xj)+abs(yi-yj)==1):
                heappush(hq,(xj,yj,ci))
            else:
                heappush(hq,(xj,yj,ci+1))

print(cost[dh][dw])
# print(cost)
