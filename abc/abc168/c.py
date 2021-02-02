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

import math

a,b,h,m = map(int,input().split())
m = m + 60*h
deg = (5.5 * m)%360
ans = (a - b * math.cos(math.radians(deg)))**2 + (b * math.sin(math.radians(deg)))**2
ans = ans**0.5

print(ans)
