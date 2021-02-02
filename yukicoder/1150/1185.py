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
ans = min(100,n)//3 - 10//3

d = deque()
for i in [3,6,9]:
    for j in [0,3,6,9]:
        d.append(i*10+j)

while(True):
    i = d.popleft()
    for j in [0,3,6,9]:
        x = i*10+j
        if(x > n):
            print(ans)
            exit()
        ans += 1
        d.append(x)
