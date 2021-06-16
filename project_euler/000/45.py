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
f = open('p042_words.txt', 'r')
sys.stdin = f

t,p,h = 286,166,143
tx = t * (t+1) // 2
px = p * (3*p-1) // 2
hx = h * (2*h-1)
while(t < 1000000):
    if tx < px or tx < hx:
        t += 1
        tx = t * (t+1) // 2
        continue
    if px < tx or px < hx:
        p  += 1
        px = p * (3*p-1) // 2
        continue
    if hx < tx or hx < px:
        h += 1
        hx = h * (2*h-1)
        continue
    print(t,p,h,tx)
    break


















