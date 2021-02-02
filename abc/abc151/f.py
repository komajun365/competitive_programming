# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import numpy as np

n = int(input())
xy = np.array([tuple(map(int,input().split())) for _ in range(n)])

if(n==2):
    a,b = xy
    ans = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    print(ans/2)
    exit()

def calc_rad(i,j,k):
    a,b,c = xy[i],xy[j],xy[k]
    g = calc_g(a,b,c)
    d = 0
    for tmp in [a,b,c]:
        d = max(d, (g[0]-tmp[0])**2 + (g[1]-tmp[1])**2)

    for tmp in xy:
        d_tmp = (g[0]-tmp[0])**2 + (g[1]-tmp[1])**2
        if( d_tmp > d ):
            return 2000
    return d**0.5

def calc_g(ra,rb,rc):
    A = np.dot(rb-rc,rb-rc)
    B = np.dot(rc-ra,rc-ra)
    C = np.dot(ra-rb,ra-rb)

    T = A*(B+C-A)
    U = B*(C+A-B)
    W = C*(A+B-C)

    if(T + U + W)==0:
        rab = (ra+rb)/2
        rac = (ra+rc)/2
        rbc = (rb+rc)/2
        if(sum(rab) <= sum(rac) <= sum(rbc))|(sum(rab) >= sum(rac) >= sum(rbc)):
            return rac
        elif(sum(rab) <= sum(rbc) <= sum(rac))|(sum(rab) >= sum(rbc) >= sum(rac)):
            return rbc
        else:
            return rab

    rcc = (T*ra + U*rb + W*rc)/(T + U + W)
    return rcc

ans = 2000
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            ans = min(ans,  calc_rad(i,j,k))

print(ans)
