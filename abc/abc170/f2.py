import sys
read = sys.stdin.read
from collections import deque

h,w,k,rs,cs,rt,ct,*s = read().split()
h,w,k,rs,cs,rt,ct = map(int,(h,w,k,rs,cs,rt,ct))
rs,cs,rt,ct = map(lambda x: x-1, (rs,cs,rt,ct))

inf = 10**7
dep = [[inf] * (w+1) for _ in range(h+1)]
for i in range(h):
    dep[i][-1] = -1
    for j in range(w):
        if s[i][j] == '@':
            dep[i][j] = -1
for j in range(w+1):
    dep[-1][j] = -1

dq = deque()
dq.append((rs,cs))
dep[rs][cs] = 0
while dq:
    x0,y0 = dq.popleft()
    d = dep[x0][y0] + 1
    for dx,dy in zip([-1,1,0,0],[0,0,-1,1]):
        x,y = x0,y0
        for _ in range(k):
            x += dx
            y += dy
            if dep[x][y] < d:
                break
            elif dep[x][y] == d:
                continue
            dep[x][y] = d
            dq.append((x,y))

if dep[rt][ct] == inf:
    print(-1)
else:
    print(dep[rt][ct])