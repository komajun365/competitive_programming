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

n,*xy = map(int,read().split())
width = max(xy) - min(xy)
lim = (width//(n-1))+1

if(n < 10**2):
    import heapq
    hq = []
    for i in range(n-1):
        xi,yi = xy[i*2:i*2+2]
        for j in range(i+1,n):
            xj,yj = xy[j*2:j*2+2]
            dif = [[abs(xi-xj),0],[abs(xi-yj),1],[abs(yi-xj),2],[abs(yi-yj),3]]
            dif.sort(key=lambda x:x[0])
            for d,num in dif[:3]:
                bi =
                heappush(hq,)
