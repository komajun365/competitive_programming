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

from decimal import *

def calc(r):
    res = Decimal(0.000000000000000000000)
    r_exp = Decimal(1.000000000000000000000)
    for k in range(1,5001):
        res += r_exp * (900-3*k)
        r_exp *= r
    return res

up = Decimal(1.000000000000000000000)
down = Decimal(1.010000000000000000000)

target = Decimal(-6.000000000000000000000*10**11)

for _ in range(200):
    mid = (up+down)/2
    if(calc(mid) > target):
        up = mid
    else:
        down = mid

print(mid)
print(calc(mid))

'''
二分探索でよい？

'''



def calc(r):
    res = 0
    r_exp = 1
    for k in range(1,5001):
        res += r_exp * (900-3*k)
        r_exp *= r
    return res

up = 1
down = 1.01

target = -6 * 10**11

for _ in range(200):
    mid = (up+down)/2
    if(calc(mid) > target):
        up = mid
    else:
        down = mid

print(mid)
print(calc(mid))
