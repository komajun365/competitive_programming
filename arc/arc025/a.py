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

d = list(map(int,input().split()))
j = list(map(int,input().split()))

ans = 0
for di,ji in zip(d,j):
    ans += max(di,ji)
print(ans)
