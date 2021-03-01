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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

n = 10**6

ans = 0
for i in range(1,n,2):
    si = str(i)
    if si == si[::-1]:
        bi = str(bin(i))[2:]
        if bi == bi[::-1]:
            ans += i

print(ans)
