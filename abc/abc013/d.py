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

n,m,d = map(int,input().split())
a = list(map(int,input().split()))

goal = list(range(n+1))
for ai in a:
    goal[ai],goal[ai+1] = goal[ai+1],goal[ai]

dbl = [[0] * 35 for _ in range(n+1)]
for i,gi in enumerate(goal):
    dbl[gi][0] = i

for j in range(1,35):
    for i in range(1,n+1):
        dbl[i][j] = dbl[ dbl[i][j-1] ][j-1]

d_bit = []
for i in range(35):
    if((d>>i)&1):
        d_bit.append(i)

ans = []
for i in range(1,n+1):
    for j in d_bit:
        i = dbl[i][j]
    ans.append(i)

print('\n'.join(map(str,ans)))
