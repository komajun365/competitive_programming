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
import math
import bisect

n,*data = map(int,read().split())
it = iter(data)
xy = [[x,y] for x,y in zip(it,it)]
eps = 10**(-10)
# eps = 0


def calc(i):
    x0,y0 = xy[i]
    degs = []
    for j in range(n):
        if i == j:
            continue
        x,y = xy[j]
        x -= x0
        y -= y0
        degs.append(math.atan2(y, x))
    
    degs.sort()
    degs += [d + 2 * math.pi for d in degs]

    res = 0
    for j in range(n-1):
        d0 = degs[j]
        d1 = degs[bisect.bisect_left(degs, d0+math.pi+eps) - 1]
        res = max(res, d1-d0)
    
    return res

ans = 0
for i in range(n):
    ans = max(ans, calc(i))

print(math.degrees(ans))