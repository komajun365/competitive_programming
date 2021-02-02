# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from collections import deque
from gc import collect

w,h = map(int,input().split())
n = int(input())
tapes =  [list(map(int,input().split())) for _ in range(n)]

# まずは座標圧縮 O(NlogN)
set_x = {0,w}
set_y = {0,h}
for tape in tapes:
    set_x.add(tape[0])
    set_x.add(tape[2])
    set_y.add(tape[1])
    set_y.add(tape[3])

list_x = sorted(list(set_x))
list_y = sorted(list(set_y))

del set_x
del set_y

collect()

dic_x = {}
dic_y = {}
for list_, dic_ in zip([list_x, list_y], [dic_x, dic_y]):
    for i,val in enumerate(list_):
        dic_[val] = i

for i in range(n):
    x1,y1,x2,y2 = tapes[i]
    tapes[i][0] = dic_x[x1]
    tapes[i][1] = dic_y[y1]
    tapes[i][2] = dic_x[x2]
    tapes[i][3] = dic_y[y2]

del dic_x
del dic_y

# imos法でテープの張られていない領域を求める O(N^2)
w = len(list_x)-1
h = len(list_y)-1

del list_x
del list_y
collect()

imos = [[0] * (w+1) for _ in range(h+1)]

for tape in tapes:
    x1,y1,x2,y2 = tape
    imos[y1][x1] += 1
    imos[y1][x2] += -1
    imos[y2][x1] += -1
    imos[y2][x2] += 1

del tapes
collect()

for i in range(h+1):
    for j in range(1,w+1):
        imos[i][j] += imos[i][j-1]

collect()

for i in range(1,h+1):
    for j in range(w+1):
        imos[i][j] += imos[i-1][j]

collect()

for i in range(h+1):
    for j in range(w+1):
        imos[i][j] = (imos[i][j]>0)

collect()

ans = 0
for i in range(h):
    for j in range(w):
        if(imos[i][j]):
            continue
        ans += 1
        d = deque()
        d.append((i,j))
        imos[i][j] = True
        while(d):
            i0,j0 = d.pop()
            for x,y in zip([1,-1,0,0],[0,0,1,-1]):
                i1,j1 = i0+y,j0+x
                if(0<=i1<h)&(0<=j1<w)&(not imos[i1][j1]):
                    d.append((i1,j1))
                    imos[i1][j1]=True
        if(ans%10==0):
            collect()

print(ans)

# 実装25分、バグとり30分
# テープ右上の座標と、imosで扱うべき座標をうまく整理できていなかった
# →　49~52行目でx2,y2をx2+1,y2+1にしてしまっていた。


# for i in imos:
#     print(i)
