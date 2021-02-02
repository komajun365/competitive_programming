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

n,a,b = map(int,input().split())
x = list(map(int,input().split()))

cango = [[0,0,0,0] for _ in range(n)]
ll,l,r,rr = 0,0,0,0
for i,xi in enumerate(x):
    while(x[ll] < xi-b):
        ll += 1
    while(x[l] < xi-a):
        l += 1
    while(x[r] < xi+a):
        r += 1
    while(x[rr] < xi+b):
        rr += 1
    cango[i] = [ll,l,r,rr]

done = [0]*n
ans = [0]*n
for i in range(n):
    gr = set()
    if(done[i]==1):
        continue
    imos = [0]*(n+1)
    imos[i] += 1
    imos[i-1] -= 1
    lim = cango[i][3]
    ind = i
    while(ind < lim):
        if(ind != 0):
            imos[ind] += imos[ind-1]
        if(imos[ind] <= 0):
            continue
        done[ind] += 1
        gr.add(ind)
        r,rr = cango[i][2:4]
        imos[r] += 1
        imos[rr] -= 1
        ll,l = cango[rr][0:2]
        imos[ll] += 1
        imos[l] -= 1
        ind += 1
        
