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
c = read().split()

pict = [[0] * (w+2) for _ in range(h+2)]
for i in range(h):
    for j in range(w):
        if(c[i][j] == 'o'):
            pict[i+1][j+1] = 1

ans = [0,0,0,0]
alp = [3] * (10**6)
for i,x in zip([0,1,2],[12,16,11]):
    for j in range(1,1001):
        num = x * j**2
        if(num >= 10**6):
            break
        alp[num] = i

for i in range(1,h+1):
    for j in range(1,w+1):
        if(pict[i][j] == 0):
            continue

        stack = [[i,j]]
        pict[i][j] = 0
        size = 1
        while(stack):
            i0,j0 = stack.pop()
            for i1,j1 in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]):
                i1 += i0
                j1 += j0
                if(pict[i1][j1] == 1):
                    pict[i1][j1] = 0
                    size += 1
                    stack.append([i1,j1])
        ans[alp[size]] += 1

print(*ans[:3])
