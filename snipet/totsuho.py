# https://atcoder.jp/contests/agc021/tasks/agc021_b
# 必要ならライブラリにします

import sys
read = sys.stdin.buffer.read
from math import atan2,pi

n,*data = map(int,read().split())

xy = [[data[i*2],data[i*2+1],i] for i in range(n)]

def calc(points):
    n = len(points)
    res = [points[0][::], points[1][::]]
    for x2,y2,i2 in points[2:]:
        while len(res) > 1:
            x1,y1,i1 = res.pop()
            x0,y0,i0 = res[-1]
            if x0 == x1 == x2:
                continue
            elif x0 == x1:
                res.append([x1,y1,i1])
                break
            elif (y1-y0)*(x2-x0) <= (y2-y0)*(x1-x0):
                continue
            else:
                res.append([x1,y1,i1])
                break
        res.append([x2,y2,i2])
    return res

def get_outers(points):
    points.sort()
    up = calc(points)

    points2 = [[-x,-y,i] for x,y,i in points[::-1]]
    down = calc(points2)
    down = [[-x,-y,i] for x,y,i in down]

    return up[:-1] + down[:-1]

outer = get_outers(xy)
l = len(outer)

ans = [0] * n
for i in range(-1,l-1):
    x0,y0,i0 = outer[i-1]
    x1,y1,i1 = outer[i]
    x2,y2,i2 = outer[i+1]
    rad1 = atan2( x2-x1, -(y2-y1))
    rad2 = atan2( x1-x0, -(y1-y0))
    if rad1 > rad2:
        rad2 += pi*2
    dif = rad2 - rad1
    ans[i1] = dif / (pi*2)

print('\n'.join(map(str,ans)))