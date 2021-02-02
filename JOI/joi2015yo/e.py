# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討7分　実装22分 バグとり8分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from collections import deque

h,w = map(int,readline().split())
a = [  list(  0 if j=='.' else int(j)  for j in i )  for i in read().split()]

stack_0 = deque()
done = set()
for i in range(h):
    for j in range(w):
        if(a[i][j] == 0):
            stack_0.append((i,j))
            done.add((i,j))

ans = 0
while(True):
    check = set()
    while(stack_0):
        i,j = stack_0.pop()
        for x,y in zip([-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]):
            x += i
            y += j
            if(0<=x<h)&(0<=y<w)&(not (x,y) in done):
                check.add((x,y))

    delete = set()
    for i,j in check:
        num = 0
        for x,y in zip([-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]):
            x += i
            y += j
            if(0<=x<h)&(0<=y<w):
                num += ((x,y) in done)
        if(num >= a[i][j]):
            delete.add((i,j))

    for i,j in delete:
        # a[i][j] = 0
        stack_0.append((i,j))
        done.add((i,j))

    if(not delete):
        break

    ans += 1

print(ans)


'''
方針
１．もともと更地マスの周囲8つについて、次の波で更地になるかチェックする
２．新しく更地になったマスの周囲8つについて、次の波で更地になるかチェックする
移行繰り返し

更地チェックはO(8)
一つのマスは1回しか更地にならないので、更地チェックが起きる回数はO(8*HW)
結局全体でO(64*HW)なので間に合う。
'''
