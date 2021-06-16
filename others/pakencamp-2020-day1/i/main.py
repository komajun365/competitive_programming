# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.read

h,w = map(int,input().split())
sx,sy,gx,gy = map(lambda x: int(x)-1,input().split())
s = read().split()
inf = 10**8

def solve(first):
    axis = first
    start = sx*w+sy
    stack = [start]
    depth = [inf] * (h*w)
    depth[start] = 0
    while stack:
        stack2 = []
        for i in stack:
            x,y = divmod(i, w)
            if axis == 0:
                dxy = [[-1,0],[1,0]]
            else:
                dxy = [[0,-1],[0,1]]
            for dx,dy in dxy:
                dx += x
                dy += y
                if not (0 <= dx < h) or not (0 <= dy < w):
                    continue
                xy = dx*w+dy
                if depth[xy] != inf:
                    continue
                if s[dx][dy] == '#':
                    continue
                depth[xy] = depth[i] + 1
                stack2.append(xy)
        stack,stack2 = stack2,stack
        axis = 1-axis
    
    return depth[gx*w+gy]

ans = min(solve(0), solve(1))
if ans == inf:
    print(-1)
else:
    print(ans)

# print(solve(0))
# print(solve(1))