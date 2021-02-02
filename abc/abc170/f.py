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

h,w,k = map(int,readline().split())
x1,y1,x2,y2 = map(int,readline().split())

c = read().split()
inf = 10**7
cost = [[inf] * (w+2) for _ in range(h+2)]
for i in range(h):
    for j in range(w):
        if(c[i][j] == '@'):
            cost[i+1][j+1] = -1

for i in range(h+2):
    cost[i][0] = -1
    cost[i][-1] = -1

for j in range(w+2):
    cost[0][j] = -1
    cost[-1][j] = -1

cost[x1][y1] = 0
stack = [(x1,y1)]

cnt = 0
while(stack):
    cnt += 1
    next = set()
    while(stack):
        x,y = stack.pop()
        for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
            for j in range(1,k+1):
                jx = x + dx*j
                jy = y + dy*j
                if(cost[jx][jy] < cnt):
                    break
                next.add((jx,jy))

    for jx,jy in next:
        cost[jx][jy] = cnt
        stack.append((jx,jy))

if(cost[x2][y2]==inf):
    print(-1)
else:
    print(cost[x2][y2])
