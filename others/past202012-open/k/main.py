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

s = [input() for _ in range(4)]
start = 0
for i in range(16):
    x = i//4
    y = i%4
    if s[x][y] == '#':
        start += 1<<i

from functools import lru_cache
@lru_cache(maxsize=10**9)
def calc(x):
    if x == 0:
        return 0
    
    res = 100
    for i in range(4):
        for j in range(4):
            miss = 0
            tmp = 5
            for i2,j2 in zip([0,0,0,1,-1],[0,1,-1,0,0]):
                i2 += i
                j2 += j
                if i2 < 0 or i2 > 3 or j2 < 0 or j2 > 3:
                    miss += 1
                    continue
                ij2 = i2*4 + j2
                if (x >> ij2) & 1 == 0:
                    miss += 1
                    continue
                tmp += calc(x ^ (1<<ij2))
            if miss == 5:
                continue
            tmp /= 5-miss
            res = min(res,tmp)
    return res

ans = calc(start)
print(ans)


