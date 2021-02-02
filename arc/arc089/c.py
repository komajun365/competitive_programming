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

n = map(int,readline().split())
data = list(map(int,read().split()))

t,x,y = 0,0,0
it = iter(data)
for ti,xi,yi in zip(it,it,it):
    dif = abs(x-xi) + abs(y-yi)
    if(ti-t < dif)|(dif%2 != (ti-t)%2):
        print('No')
        exit()
    t,x,y = ti,xi,yi
print('Yes')
