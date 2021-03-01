# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read

n,m,*xy = map(int,read().split())
red = [0] * n
red[0] = 1
cnt = [1] * n

it = iter(xy)
for x,y in zip(it,it):
    x -= 1
    y -= 1
    if red[x] == 1:
        red[y] = 1
    if cnt[x] == 1:
        red[x] = 0
    cnt[x] -= 1
    cnt[y] += 1

print(sum(red))