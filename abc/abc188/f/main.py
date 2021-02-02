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
sys.setrecursionlimit(10**9)
from functools import lru_cache

x,y = map(int,input().split())

@lru_cache(maxsize=10**9)
def calc(a):
    if a <= x:
        return x-a
    res = a - x
    if a % 2 == 0:
        res = min(res, calc(a//2)+1)
    else:
        res = min(res, calc(a//2)+2, calc((a+1)//2)+2)
    return res

ans = calc(y)
print(ans)