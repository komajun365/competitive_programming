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

n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
    x0,y0 = xy[i]
    for j in range(i+1,n):
        x1,y1 = xy[j]
        ans = max(ans, (x0-x1)**2 + (y0-y1)**2)

print(ans**0.5)
