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

from heapq import heappop,heappush
from collections import deque

import sys
read = sys.stdin.buffer.read

q,*query = map(int,read().split())

hq = []
tail = deque()

ans = []
idx = 0
for _ in range(q):
    if query[idx] == 1:
        tail.append(query[idx+1])
        idx += 2
    elif query[idx] == 2:
        if hq:
            ans.append(heappop(hq))
        else:
            ans.append(tail.popleft())
        idx += 1
    else:
        while tail:
            heappush(hq, tail.popleft())
        idx += 1

if ans:
    print('\n'.join(map(str,ans)))
