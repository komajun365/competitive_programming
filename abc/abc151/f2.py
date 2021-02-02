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
import itertools

n = int(readline())
xy = tuple(map(int,read().split()))

#解説ACです

def check(d):
    eps = 1/(10**10)
    points = []
    for c in itertools.combinations(range(n),2):
        x1,y1 = xy[c[0]*2 : c[0]*2+2]
        x2,y2 = xy[c[1]*2 : c[1]*2+2]

        dif = (x1-x2)**2 + (y1-y2)**2
        if(dif > 4*d**2):
            return False

        h = (d**2 - dif/4)**0.5
        xm,ym = (x1+x2)/2, (y1+y2)/2

        dx,dy = (y1-y2), -1*(x1-x2)
        dxy = (dx**2 + dy**2)**0.5

        points.append( (xm + dx*h/dxy, ym + dy*h/dxy)  )
        points.append( (xm - dx*h/dxy, ym - dy*h/dxy)  )

    for xp,yp in points:
        for i in range(n):
            xi,yi = xy[i*2:i*2+2]
            dif = (xp-xi)**2 + (yp-yi)**2
            if(dif > d**2 + eps):
                break
        else:
            return True

    return False

ok = 1000
ng = 0
for _ in range(50):
    mid = (ok+ng)/2
    if(check(mid)):
        ok = mid
    else:
        ng = mid

print(ok)
# print(ok,ng,mid)




'''
任意の3点を中心に半径dの円を描いて、
重なり合う部分があればよい？



'''
