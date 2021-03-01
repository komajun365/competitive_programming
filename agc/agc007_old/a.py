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

h,w = map(int,input().split())
a = [input() for _ in range(h)]

cnt = 0
for x in range(h):
    for y in range(w):
        cnt += (a[x][y]=='#')
if(cnt > h+w-1):
    print('Impossible')
    exit()


x,y = 0,0
while(x+y<h+w-2):
    dx,dy=0,0

    if(x!=h-1):
        if(a[x+1][y]=='#'):
            dx = 1
    if(y!=w-1):
        if(a[x][y+1]=='#'):
            dy = 1
    if(dx+dy!=1):
        print('Impossible')
        exit()

    x += dx
    y += dy

print('Possible')
