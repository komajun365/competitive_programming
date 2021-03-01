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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

from math import gcd

child = 1
mother = 1

for x in range(1,10):
    for a in range(10):
        for b in range(10):
            xa = x*10+a
            ax = a*10+x
            xb = x*10+b
            bx = b*10+x
            if bx >= 10 and xa < bx:
                if xa * b == bx*a:
                    print(xa,bx)
                    child *= xa
                    mother *= bx
            if ax >= 10 and ax < xb:
                if ax * b == xb*a:
                    print(ax,xb)
                    child *= ax
                    mother *= xb

print(mother // gcd(child,mother))


'''
xa/bx == a/b
ax/xb == a/b
いずれかを全探索

'''
