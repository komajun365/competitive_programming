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

p = float(input())
print(p/(1-p))


'''

e = 0*(1-p) + p(1+e)
e = p + pe
0 = p + e(p-1)
e = p/(1-p)

'''
