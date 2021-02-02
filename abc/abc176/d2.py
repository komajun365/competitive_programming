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
from collections import deque

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

inf = 10**10
cost = [[inf] * w for _ in range(h)]
cost[ch][cw]=0
d = deque()
d.append((0,ch,cw))

while(d):
    ci,xi,yi = d.popleft()
    if(cost[xi][yi] > ci):
        continue

    for dx in range(-2,3):
        xj = xi+dx
        if(xj<0)|(xj>=h):
            continue
        for dy in range(-2,3):
            yj = yi+dy
            # print(xi,yi,xj,yj)
            if(yj<0)|(yj>=w):
                continue
            if(xi==xj)&(yi==yj):
                continue
            if(wall[xj][yj]==1):
                continue
            if(abs(xi-xj)+abs(yi-yj)==1):
                if(cost[xj][yj] > ci):
                    cost[xj][yj] = ci
                    d.appendleft((ci,xj,yj))
            else:
                if(cost[xj][yj] > ci+1):
                    cost[xj][yj] = ci+1
                    d.append((ci+1,xj,yj))

if(cost[dh][dw] == inf):
    print(-1)
else:
    print(cost[dh][dw])
# print(cost)
