import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from scipy.sparse.csgraph import csgraph_from_dense,floyd_warshall

h,w = map(int, input().split())
s = [input() for _ in range(h) ]

d = [[10**9] * (w*h) for _ in range(w*h)]

for i in range(h):
    for j in range(w):
        if(s[i][j] == '.'):
            if(i != h-1):
                if(s[i+1][j] == '.'):
                    d[(i*w + j)][((i+1)*w + j)] = 1
                    d[((i+1)*w + j)][(i*w + j)] = 1
            if(j != w-1):
                if(s[i][j+1] == '.'):
                    d[(i*w + j)][(i*w + j + 1)] = 1
                    d[(i*w + j + 1)][(i*w + j)] = 1

G = csgraph_from_dense(d, null_value=10**9)
len = floyd_warshall(G)

ans = 0
for i in range(h*w):
    for j in range(h*w):
        if(len[i][j] < 1000000):
            ans = max(len[i][j], ans)

print(int(ans))
