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

# import itertools

n = int(input())
t = []
for _ in range(n):
    t.append(int(input()))

ans = sum(t)
for i in range(2**n):
    time = [0,0]
    for j in range(n):
        time[(i>>j)&1] += t[j]
    ans = min(ans, max(time))

print(ans)
