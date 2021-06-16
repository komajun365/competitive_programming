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

H,W,h,w = map(int,input().split())

if(H%h==0)&(W%w==0):
    print('No')
    exit()

print('Yes')

if(W%w!=0):
    base = [1000] * (w-1) + [-1000 * (w-1) -1]
    col = []
    for i in range(1 + W//w):
        col = col + base
    col = col[:W]
    for i in range(H):
        print(' '.join(map(str,col)))

else:
    base = [1000] * (h-1) + [-1000 * (h-1) -1]
    row = []
    for i in range(1 + H//h):
        row = row + base
    row = row[:H]
    for i in row:
        col = [i] * W
        print(' '.join(map(str,col)))


'''
縦か横で市松模様的にできればいい？
たぶん、ぴったし分割できないとき以外は行ける。

'''
