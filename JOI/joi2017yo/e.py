# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討13分　実装13分 バグとり1分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

h,w = map(int, readline().split())
height = [ list( map(int, i.split()))  for i in readlines()]

h_map = [0] * (h*w+1)
for i in range(h):
    for j in range(w):
        h_map[height[i][j]] = (i,j)

flow = [[-1] * w for _ in range(h)]

inf = 10**10
ans = 0
for i,(x,y) in enumerate(h_map[1:],1):
    if(flow[x][y] == -1):
        flow[x][y] = i
    elif(flow[x][y] == inf):
        ans += 1
    for dx,dy in zip([0,0,-1,1],[-1,1,0,0]):
        dx +=x
        dy +=y
        if(0<=dx<h)&(0<=dy<w):
            if(height[dx][dy] > i):
                if(flow[dx][dy] == -1):
                    flow[dx][dy] = flow[x][y]
                elif(flow[dx][dy] != flow[x][y]):
                    flow[dx][dy] = inf

print(ans)

'''
全ての区域について、流れ出る先の標高を求めてやればいい。
標高が低いところから決めていくとうまくいく。
'''
