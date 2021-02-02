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
it = iter(data)
xytr = []
for x,y,t,r in zip(it,it,it,it):
    xytr.append([x,y,t,r])

if(n==1):
    print(0)
    exit()

inf = 10**6
d = [inf] * n
d[0] = 0
rem = set(range(n))
for _ in range(n):
    next = -1
    next_d = inf+1
    for i in rem:
        if(d[i] < next_d):
            next = i
            next_d = d[i]
    rem.remove(next)

    xi,yi,ti,ri = xytr[next]
    for j in rem:
        xj,yj,tj,rj = xytr[j]
        dif = ((xi-xj)**2 + (yi-yj)**2)**0.5
        time = dif / min(ti,rj)
        d[j] = min(d[j], d[next] + time)

d = d[1:]
d.sort()

for i in range(n-1):
    d[n-2-i] += i
print(max(d))
