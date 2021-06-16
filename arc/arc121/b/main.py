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

n,*ac = read().split()
n = int(n)
inf = 10**18

rgb = [[] for _ in range(3)]
d = {'R':0, 'G':1, 'B':2}
it = iter(ac)
for a,c in zip(it,it):
    a = int(a)
    rgb[d[c]].append(a)

for i in range(3):
    rgb[i].sort()

if len(rgb[0]) % 2 == 0 and len(rgb[1]) % 2 == 0:
    print(0)
    exit()

def calc(x,y):
    res = [[-1,inf],[-1,inf]]
    lx = len(x)
    y = [-1*inf] + y + [inf]
    ly = len(y)

    if lx == 0 or ly == 2:
        return res
    
    idx = 1
    for i in range(lx):
        while y[idx] < x[i]:
            idx += 1
        near = min(y[idx] - x[i], x[i] - y[idx-1])
        if near < res[0][1]:
            res[1] = res[0][::]
            res[0] = [i,near]
        elif near < res[1][1]:
            res[1] = [i,near]
    
    return res

if len(rgb[1]) % 2 == 0:
    rgb[0],rgb[1] = rgb[1],rgb[0]
elif len(rgb[2]) % 2 == 0:
    rgb[0],rgb[2] = rgb[2],rgb[0]

ans = calc(rgb[1],rgb[2])[0][1]

xy = calc(rgb[0],rgb[1])
xz = calc(rgb[0],rgb[2])
if xy[0][0] != xz[0][0]:
    ans = min(ans, xy[0][1] + xz[0][1])
else:
    ans = min(ans, xy[0][1] + xz[1][1], xy[1][1] + xz[0][1])

print(ans)
