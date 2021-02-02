# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# https://www.ioi-jp.org/camp/2008/2008-sp-tasks/2008-sp_tr-day1_20.pdf
# 検討12分　実装30分 バグとり13分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f


import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
d = int(input())
k = int(input())

city = [list(map(int,input().split())) for _ in range(n)]
width = 1000 + 1
area_n = 1 + (width-1)//d
area = [ [] for i in range(area_n) ]
for i in range(area_n):
    area[i] = [ set() for _ in range(area_n) ]

# JOI市は最初から除いておく
for i,c in enumerate(city[1:],2):
    x,y = c
    area[x//d][y//d].add(i)

inf = 101
start = [inf] * (n+1)
deq = deque()
deq.append((1,0))

while(deq):
    c,day = deq.popleft()
    if(day > k):
        break
    start[c] = day
    cx, cy = city[c-1]
    area_x = cx// d
    area_y = cy// d
    removes = set()
    for x in range( max(0,area_x-1), min(area_n-1, area_x+1)+1 ):
        for y in range( max(0,area_y-1), min(area_n-1, area_y+1)+1 ):
            for c1 in area[x][y]:
                cx1,cy1 = city[c1-1]
                d_tmp = (cx-cx1)**2 + (cy-cy1)**2
                if(d_tmp <= d**2):
                    deq.append((c1,day+1))
                    removes.add((c1, cx1//d , cy1//d))

    for rem in removes:
        c1,x,y = rem
        area[x][y].remove(c1)

ans = 0
for i in start[1:]:
    ans += (i<=k)&(k<=(i+m-1))

print(ans)
