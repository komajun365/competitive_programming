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
    if(done[i]==1):
        continue

    gr = set()
    l1,r1 = i,i
    l2 = cango[l1][2]
    r2 = 0

    while(True):
        r2 = cango[r1][3] - 1
        r1 = cango[r2][1] - 1
        if(l1 == r2):
            gr.add(l1)
            break
        if(r1 >= l1):
            l1 =
