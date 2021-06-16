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
read = sys.stdin.buffer.read
import itertools

n,*data = map(int,read().split())
a = data[:n*n]
m = data[n*n]
xy = data[n*n+1:]

bad = [[0]*n for _ in range(n)]
it = iter(xy)
for x,y in zip(it,it):
    x -= 1
    y -= 1
    bad[x][y] = 1
    bad[y][x] = 1

inf = 10**9
ans = inf
for p in itertools.permutations(range(n)):
    p = list(p)
    for i in range(n-1):
        if bad[p[i]][p[i+1]] == 1:
            break
    else:
        tot = 0
        for i in range(n):
            tot += a[p[i] * n + i]
        ans = min(ans,tot)

if ans == inf:
    print(-1)
else:
    print(ans)

