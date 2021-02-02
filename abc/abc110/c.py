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

s = input()
t = input()

d = {}
use = set()
for si,ti in zip(s,t):
    if(si in d):
        if(ti != d[si]):
            print('No')
            exit()
    else:
        if(ti in use):
            print('No')
            exit()
        d[si] = ti
        use.add(ti)

print('Yes')
