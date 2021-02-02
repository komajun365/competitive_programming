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

n,m = map(int, readline().split())
data = list(map(int, read().split()))

point = [{0,10**9,-1*10**9} for _ in range(2)]
dic_en = [{} for _ in range(2)]
dic_de = [{} for _ in range(2)]

it = iter(data[:3*n])
for a,b,c in zip(it,it,it):
    point[0].add(a)
    point[0].add(b)
    point[1].add(c)

it = iter(data[3*n:])
for d,e,f in zip(it,it,it):
    point[0].add(d)
    point[1].add(e)
    point[1].add(f)

for i,p in enumerate(point):
    p = sorted(list(p))
    for after,before in enumerate(p):
        dic_en[i][before] = after
        dic_de[i][after] = before

len_x = len(point[0])
len_y = len(point[1])

wall_x = [[0] * (len_y-1) for _ in range(len_x)]
wall_y = [[0] * (len_y) for _ in range(len_x-1)]

it = iter(data[:3*n])
for a,b,c in zip(it,it,it):
    a,b,c = dic_en[0][a],dic_en[0][b],dic_en[1][c]
    wall_y[a][c] += 1
    if(b != len_x-1):
        wall_y[b][c] -= 1

it = iter(data[3*n:])
for d,e,f in zip(it,it,it):
    d,e,f = dic_en[0][d],dic_en[1][e],dic_en[1][f]
    wall_x[d][e] += 1
    if(f != len_y-1):
        wall_x[d][f] -= 1

for i in range(len_x):
    for j in range(1,len_y-1):
        wall_x[i][j] += wall_x[i][j-1]

for i in range(1,len_x-1):
    for j in range(len_y):
        wall_y[i][j] += wall_y[i-1][j]

start = (dic_en[0][0], dic_en[1][0])
area = [[0] * (len_y-1) for _ in range(len_x-1)]

ans = 0
stack = [start]
i,j = start
area[i][j] = 1
while(stack):
    i,j = stack.pop()
    ans += (dic_de[0][i+1] - dic_de[0][i])*(dic_de[1][j+1] - dic_de[1][j])
    #x+
    if(wall_x[i+1][j]==0):
        if(i==len_x-2):
            print('INF')
            exit()
        if(area[i+1][j] == 0):
            stack.append((i+1,j))
            area[i+1][j] = 1
    #x-
    if(wall_x[i][j]==0):
        if(i==0):
            print('INF')
            exit()
        if(area[i-1][j] == 0):
            stack.append((i-1,j))
            area[i-1][j] = 1
    #y+
    if(wall_y[i][j+1]==0):
        if(j==len_y-2):
            print('INF')
            exit()
        if(area[i][j+1] == 0):
            stack.append((i,j+1))
            area[i][j+1] = 1

    #y-
    if(wall_y[i][j]==0):
        if(j==0):
            print('INF')
            exit()
        if(area[i][j-1] == 0):
            stack.append((i,j-1))
            area[i][j-1] = 1

print(ans)

# print(dic_de[0])
# print(dic_de[1])
# for i in wall_y:
#     print(i)
