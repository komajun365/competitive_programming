# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討6分　実装17分 バグとり18分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

# ヒープキュー（最小値・最大値の取得）
from heapq import heappop,heappush

h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]

inf = 10**10
dist_max = h*w
area = [[0] * (w+2) for _ in range(h+2)]
for i in range(h+2):
    for j in range(w+2):
        area[i][j] = [inf]*dist_max

a2 = [[inf] * (w+2) for _ in range(h+2)]
for i in range(1,h+1):
    for j in range(1,w+1):
        a2[i][j] = a[i-1][j-1]

hq = [(0,0,1,1)]
while hq:
    time,dist,x,y = heappop(hq)
    if(area[x][y][dist] != inf):
        continue
    area[x][y][dist] = time
    if(x==h)&(y==w):
        print(time)
        break
    if(dist==dist_max-1):
        continue
    for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
        xj = x+dx
        yj = y+dy

        if(a2[xj][yj]==inf)|(area[xj][yj][dist-1] != inf)|(area[xj][yj][dist+1] != inf):
            continue
        time_j = (dist*2 + 1)*a2[xj][yj]
        heappush(hq, (time+time_j,dist+1,xj,yj))


# for i in area:
#     print(i)

'''
拡張ダイクストラのようなもの。
i,j=(1,1)のマスにいるとき、隣り合うマス（右と下）のますを移動できるようになるまでの時間をheapに追加する。
かかる時間が最小の土地から確定していけばよい。


これだとうまくいかない。
areaの添え字にdistを入れてしまおう。
'''
