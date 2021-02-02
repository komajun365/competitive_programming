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

n,x,y = map(int,readline().split())
xy = list(map(int,read().split()))

inf = 10**7
area = [[inf] * (405) for _ in range(405)]
for i in range(405):
    area[0][i] = -1
    area[404][i] = -1
    area[i][0] = -1
    area[i][404] = -1

it = iter(xy)
for i,j in zip(it,it):
    area[i+202][j+202] = -1

area[202][202] = 0
stack = [[(202,202)],[]]
for dif in range(inf):
    while(stack[dif%2]):
        i,j = stack[dif%2].pop()
        for di,dj in zip([1,0,-1,1,-1,0],[1,1,1,0,0,-1]):
            di += i
            dj += j
            if(area[di][dj]==inf):
                area[di][dj] = dif+1
                stack[(dif+1)%2].append((di,dj))
                if(di-202==x)&(dj-202==y):
                    print(dif+1)
                    exit()

print(-1)
