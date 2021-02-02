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

n = input()

def calc(x,y,z):
    # x<= y<= zとする
    if(x+y <= z):
        return 0
    res = (x+y+z)*(x+y-z)*(x-y+z)*(-x+y+z)
    return res

ans = 0
for x in range(1,200):
    y0 = max(x, n//x)
    for y in range(y0,)
