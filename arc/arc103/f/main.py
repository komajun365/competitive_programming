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
from heapq import heappop,heappush

n,*d = map(int,read().split())
cnt = dict()

hq = []
for i,di in enumerate(d,1):
    x = (di<<40) + (1<<20) + i
    heappush(hq, x*-1)
    cnt[di] = cnt.get(di,0) + 1

while hq:
    x = heappop(hq) * -1
    di = x >> 40
    x -= di<<40
    ci = x >> 20
    i = x - (ci<<20)
    



