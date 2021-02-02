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
s = read().split()
color = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if(s[i][j] =='#'):
            color[i][j] = 1

ans = 0
done = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if(done[i][j]==1):
            continue

        cnt = [0]*2
        cnt[(i+j)%2] += 1
        done[i][j] = 1
        stack = [(i,j)]
        while(stack):
            x,y = stack.pop()
            for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
                dx += x
                dy += y
                if(0 <= dx < h)&(0 <= dy < w):
                    if(done[dx][dy] == 1):
                        continue
                    if(color[x][y] != color[dx][dy]):
                        done[dx][dy] = 1
                        stack.append((dx,dy))
                        cnt[(dx+dy)%2] += 1
        ans += cnt[0] * cnt[1]
        # print(i,j,cnt)

print(ans)
