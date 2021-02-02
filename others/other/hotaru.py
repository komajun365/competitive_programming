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

import itertools

n,s = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

h = itertools.combinations_with_replacement(range(s+1), n)

for i in h:
    cnt = [[0] * n for _ in range(n)]
