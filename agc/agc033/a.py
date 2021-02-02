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
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

h,w = map(int,readline().split())
a = read().split()

color = [[0]*(w+2) for _ in range(h+2) ]
stack = []
for i in range(h):
    for j in range(w):
        if(a[i][j] == '#'):
            color[i+1][j+1] = 1
            stack.append((i+1,j+1))

for i in range(h+2):
    color[i][0] = 1
    color[i][-1] = 1

for j in range(w+2):
    color[0][j] = 1
    color[-1][j] = 1

ans = -1
while(stack):
    ans += 1
    new_stack = []
    while(stack):
        i,j = stack.pop()
        for x,y in zip([0,0,-1,1],[-1,1,0,0]):
            x += i
            y += j
            if(color[x][y]==0):
                color[x][y] = 1
                new_stack.append((x,y))

    stack = new_stack[::]

print(ans)
