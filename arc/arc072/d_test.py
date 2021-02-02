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

n = 100
memo = [[-1] * n for _ in range(n)]
memo[0][0] = 0
memo[0][1] = 0
memo[1][0] = 0
memo[1][1] = 0

def calc(x,y):
    if(memo[x][y] != -1):
        return memo[x][y]
    if(memo[y][x] != -1):
        memo[x][y] = memo[y][x]
        return memo[x][y]

    cango = [0] * (n*2)
    for i in range(1,x//2 + 1):
        cango[calc(x-2*i,y+i)] += 1

    for i in range(1,y//2 + 1):
        cango[calc(x+i,y-2*i)] += 1

    for i,ci in enumerate(cango):
        if(ci==0):
            memo[x][y] = i
            return i

n2 = 30
for i in range(n2):
    for j in range(n2):
        calc(i,j)

for i in memo[:n2]:
    print(i[:n2])
