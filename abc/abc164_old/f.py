# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
s = list(map(int,input().split()))
t = list(map(int,input().split()))
u = list(map(int,input().split()))
v = list(map(int,input().split()))

a = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = [-1] * 64

 for i in range(n):
    si = s[i]
    ui = u[i]
    for j in range(n):
        ti = t[i]
        vi = v[i]
        if(si==0)&(ti==0):
             num = ui|vi
             for k in range(64):
                 if( (num >> k)  & 1):
                     a[i][j][k] = 1
        elif(si==1)&(ti==1):
            num = ui&vi
            for k in range(64):
                if( ((num >> k)  & 1) != 1):
                    a[i][j][k] = 0
        elif(si==0)&(ti==1):
            for k in range(64):
                uik = (ui >> k)&1
                vik = (vi >> k)&1
                if(uik==vik==1):
                    a[i][j][k] = 1
                elif(uik==vik==0):
                    a[i][j][k] = 1
                elif(uik==1)&(vik==0):
                    print(-1)
                    exit()
        else:
            for k in range(64):
                uik = (ui >> k)&1
                vik = (vi >> k)&1
                if(uik==vik==1):
                    a[i][j][k] = 1
                elif(uik==vik==0):
                    a[i][j][k] = 1
                elif(uik==0)&(vik==1):
                    print(-1)
                    exit()
