# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討2分　実装30分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k = map(int, readline().split())
data = [list(map(int, i.split())) for i in readlines() ]

point = [{0,10**6} for _ in range(3)]
dic_en = [{} for _ in range(3)]
dic_de = [{} for _ in range(3)]
for xyd in data:
    for i in range(6):
        point[i%3].add(xyd[i])

for i,p in enumerate(point):
    p = sorted(list(p))
    for after,before in enumerate(p):
        dic_en[i][before] = after
        dic_de[i][after] = before

len_x,len_y,len_d = map(len, point)
imos = [0] * (len_d)
for d in range(len_d):
    imos[d] = [[0]* len_x for _ in range(len_y)]

for xyd in data:
    for i in range(6):
        xyd[i] = dic_en[i%3][xyd[i]]

    x1,y1,d1,x2,y2,d2 = xyd
    imos[d1][y1][x1] += 1
    imos[d1][y1][x2] -= 1
    imos[d1][y2][x1] -= 1
    imos[d1][y2][x2] += 1
    imos[d2][y1][x1] -= 1
    imos[d2][y1][x2] += 1
    imos[d2][y2][x1] += 1
    imos[d2][y2][x2] -= 1

for d in range(len_d):
    for y in range(len_y):
        for x in range(1,len_x):
            imos[d][y][x] += imos[d][y][x-1]

for d in range(len_d):
    for x in range(len_x):
        for y in range(1,len_y):
            imos[d][y][x] += imos[d][y-1][x]

for y in range(len_y):
    for x in range(len_x):
        for d in range(1,len_d):
            imos[d][y][x] += imos[d-1][y][x]

ans = 0
for d in range(len_d-1):
    for y in range(len_y-1):
        for x in range(len_x-1):
            if(imos[d][y][x] >= k):
                xd = dic_de[0][x+1] -dic_de[0][x]
                yd = dic_de[1][y+1] -dic_de[1][y]
                dd = dic_de[2][d+1] -dic_de[2][d]
                ans += xd*yd*dd

print(ans)

'''
方針
座標圧縮して三次元imos
'''
