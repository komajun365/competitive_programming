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

h,w,*c = list(map(int,read().split()))
cumsum = [[0]*(w+1) for _ in range(h+1)]

for i in range(h):
    for j in range(w):
        cumsum[i][j] = cumsum[i-1][j] + c[i*w+j] * (1 - 2*((i+j) % 2))

for i in range(h):
    for j in range(w):
        cumsum[i][j] += cumsum[i][j-1]

ans = 0
for il in range(-1,h-1):
    for ir in range(il+1,h):
        for jl in range(-1,w-1):
            for jr in range(jl+1,w):
                tmp = cumsum[ir][jr] - cumsum[ir][jl] - cumsum[il][jr] + cumsum[il][jl]
                if(tmp == 0):
                    ans = max(ans, (ir-il)*(jr-jl))
print(ans)
