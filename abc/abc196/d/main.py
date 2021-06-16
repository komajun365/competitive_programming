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

h,w,a,b = map(int,input().split())
n = h*w

def calc(x,a,b):
    if x == 2**n -1:
        return 1
    for i in range(n):
        if (x>>i)&1:
            continue
        break
    res = 0
    if b > 0:
        res += calc(x | (1<<i), a, b-1)
    if a > 0:
        if x >> (i+1) & 1 == 0 and i % w != w-1:
            res += calc(x | (3<<i), a-1, b)
        if i + w < n and x >> (i+w) & 1 == 0:
            res += calc(x | (1<<i) | (1<<(i+w)), a-1, b)
    return res

ans = calc(0,a,b)
print(ans)
