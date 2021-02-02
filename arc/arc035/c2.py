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

def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

n,m = map(int,readline().split())
data = list(map(int,read().split()))
abc = data[:3*m]
k = data[3*m]
xyz = data[3*m+1:]

inf = 10**9
dist = [[inf] * (n) for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

it = iter(abc)
for a,b,c in zip(it,it,it):
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c

dist = warshall_floyd(dist,n)

tot = sum([sum(i) for i in dist])//2
ans = []

it = iter(xyz)
for x,y,z in zip(it,it,it):
    x -= 1
    y -= 1

    if(dist[x][y] <= z):
        ans.append(tot)
        continue
    dist[x][y] = z
    dist[y][x] = z


    for i in range(n-1):
        for j in range(i+1,n):
            dist[i][j] = min(dist[i][j],
                            dist[i][x] + z + dist[y][j],
                            dist[i][y] + z + dist[x][j])
            dist[j][i] = dist[i][j]

    tot = sum([sum(i) for i in dist])//2
    ans.append(tot)

print('\n'.join(map(str,ans)))
