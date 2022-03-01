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

from math import pi

n,q,*data = map(int,read().split())
xrh = data[:n*3]
ab = data[n*3:]

ans = []
it = iter(ab)
for a,b in zip(it,it):
    res = 0
    it2 = iter(xrh)
    for x,r,h in zip(it2,it2,it2):
        if x + h <= a or b <= x:
            continue
        tmp = pi * r * r * h / 3
        h1 = min(x + h - a, h)
        h2 = max(x + h - b, 0)
        tmp = tmp * (h1**3 - h2**3) / h**3
        res += tmp
    ans.append(str(res))

print('\n'.join(ans))



