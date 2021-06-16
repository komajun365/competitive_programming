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

a = list(map(int,input().split()))
tot = sum(a)
for i in range(16):
    tmp = 0
    for j in range(4):
        if(i >> j)&1:
            tmp += a[j]
    if(tmp*2==tot):
        print('Yes')
        exit()

print('No')
