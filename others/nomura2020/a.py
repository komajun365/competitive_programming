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

h1,m1,h2,m2,k = map(int,input().split())
oki = h2*60+m2 - h1*60-m1
if(oki < 0):
    oki = 60*24 - oki

print(oki - k)
