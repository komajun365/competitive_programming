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

n = int(input())
x = list(map(int,input().split()))

@lru_cache(maxsize=10**9)
def solve(bit):
    if bit == 0:
        return 0

    res = 10**9
    for i in range(16-2):
        mask = 7 << i
        if (bit & mask) == 0:
            continue
        hit = []
        for j in range(i,i+3):
            if (bit & (1<<j)) == 0:
                continue
            hit.append(solve(bit - (1<<j)))
        if len(hit) == 3:
            tmp = 1
            for hi in hit:
                tmp += hi/3
        elif len(hit) == 2:
            tmp = 3/2
            for hi in hit:
                tmp += hi/2
        else:
            tmp = 3
            for hi in hit:
                tmp += hi
        res = min(res,tmp)
    return res

bit = 0
for xi in x:
    bit |= (1<<xi)

print(solve(bit))
            







