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

from math import gcd

n,k = map(int,input().split())
a = list(map(int,input().split()))

gcd_num = a[0]
for ai in a[1:]:
    gcd_num = gcd(gcd_num,ai)

if(k%gcd_num==0)&(k <= max(a)):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')


'''

'''
