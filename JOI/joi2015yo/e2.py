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

h,w = map(int,readline().split())
a = [  list(  0 if j=='.' else int(j)  for j in i )  for i in read().split()]

stack = [[],[]]
ans = 0
for i in range(h):
    for j in range(w):
        if(a[i][j] == 0):
            stack[ans%2].append((i,j))

while(True):
    ind = ans%2
    while(stack[ind]):
        i,j = stack[ind].pop()
        for x,y in zip([-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]):
            x += i
            y += j
            if(0<=x<h)&(0<=y<w):
                if(a[x][y]==0):
                    continue
                if(a[x][y] > 0):
                    a[x][y] -= 1
                if(a[x][y]==0):
                    stack[1-ind].append((x,y))

    if(not stack[1-ind]):
        break

    ans += 1

print(ans)

'''
方針
強度＝HPだと考えて、
あるマスのHPが0になったとき、周囲の8マスに1ずつダメージを与えていくと考える。

'''
