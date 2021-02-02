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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,*data = list(map(int,read().split()))
xor = 0
i = 0
for _ in range(n):
    x,y,z,m = data[i:i+4]
    i += 4
    xl,yl,zl = x,y,z
    xr,yr,zr = 0,0,0
    for j in range(m):
        xj,yj,zj = data[i:i+3]
        i += 3
        xl = min(xl,xj)
        yl = min(yl,yj)
        zl = min(zl,zj)
        xr = max(xr,xj)
        yr = max(yr,yj)
        zr = max(zr,zj)
    xor = xor ^ (xl) ^ (yl) ^ (zl) ^ (x-xr-1) ^ (y-yr-1) ^ (z-zr-1)

if(xor==0):
    print('LOSE')
else:
    print('WIN')
