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
from heapq import heappop,heappush

t = int(readline())
q = list(map(int,read().split()))

now = 0
ans = [0] * t
for cyc in range(t):
    n = q[now]
    klr = q[now+1: now+1+3*n]
    now = now+1+3*n

    it = iter(klr)
    lc = []
    rc = []
    min_p = 0
    for x,y,z in zip(it,it,it):
        if(y==z):
            min_p += y
        elif(y>z):
            min_p += z
            lc.append((x,y-z))
        else:
            min_p += y
            rc.append((n-x,z-y))

    res = min_p
    lc.sort()
    rc.sort()

    for cam in [lc,rc]:
        hq = []
        for i in range(n,0,-1):
            if(len(cam)>0):
                while(cam[-1][0] == i):
                    x,p = cam.pop()
                    heappush(hq,p*-1)
                    if(len(cam)==0):
                        break
            if(hq):
                res += heappop(hq)*-1

    ans[cyc] = res

print('\n'.join(map(str,ans)))
