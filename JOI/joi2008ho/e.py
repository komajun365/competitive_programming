# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from collections import deque

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

# imos法でテープの張られていない領域を求める O(N^2)
w = len(list_x)-1
h = len(list_y)-1

imos = [[0] * (w+1) for _ in range(h+1)]

for tape in tapes:
    x1,y1,x2,y2 = tape
    imos[y1][x1] += 1
    imos[y1][x2] += -1
    imos[y2][x1] += -1
    imos[y2][x2] += 1

for i in range(h+1):
    for j in range(1,w+1):
        imos[i][j] += imos[i][j-1]

for i in range(1,h+1):
    for j in range(w+1):
        imos[i][j] += imos[i-1][j]

# 左右に全探索する y*10000+xを座標情報にしておく。 O(N^2)
whites = set()
for i in range(h):
    for j in range(w):
        if(imos[i][j] == 0):
            whites.add(i*10000+j)

d = deque()
ans = 0
while(whites):
    ans += 1
    start = whites.pop()
    d.append(start)
    while(d):
        now = d.pop()
        for pl in [1,-1,10000,-10000]:
            next = now + pl
            if( next in whites):
                d.append(next)
                whites.remove(next)

print(ans)

# 実装25分、バグとり30分
# テープ右上の座標と、imosで扱うべき座標をうまく整理できていなかった
# →　49~52行目でx2,y2をx2+1,y2+1にしてしまっていた。


# for i in imos:
#     print(i)
