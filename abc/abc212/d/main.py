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

q,*query = map(int,read().split())

plus = 0
idx = 0
hq = []
ans = []
for _ in range(q):
    if query[idx] == 1:
        xi = query[idx+1]
        idx += 2
        heappush(hq, xi-plus)
    elif query[idx] == 2:
        xi = query[idx+1]
        idx += 2
        plus += xi
    else:
        idx += 1
        x = heappop(hq) + plus
        ans.append(x)

print('\n'.join(map(str,ans)))


