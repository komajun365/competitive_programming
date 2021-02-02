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

### 解いてません！！！

from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int,input().split()))

@lru_cache(maxsize=10**6)
def calc_g(x):
    if(x==0):
        return 0
    elif(x <= 2):
        return 1

    gr = [0] * (x+1)
    gr[calc_g(x-2)] += 1
    gr[calc_g(x-3)] += 1
    for i in range(1,(x-1)//2):
        gr[calc_g(i) ^ calc_g(x-3-i)] += 1

    for i in range(x+1):
        if(gr[i]==0):
            return i

n = 1000
grundy = [0] * n
for i in range(n):
    grundy[i] = calc_g(i)

for i in range(n//34):
    print(grundy[i*34:(i+1)*34])
