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

from collections import deque

n = int(input())
h = list(map(int,input().split()))

ans = [0] * n
d = deque()
for i in range(n):
    ans[i] = len(d)
    while(True):
        if(len(d)==0):
            d.append(h[i])
            break
        last = d.pop()
        if(last > h[i]):
            d.append(last)
            d.append(h[i])
            break

print('\n'.join(map(str,ans)))
