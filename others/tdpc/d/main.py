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

n,d = map(int,input().split())

x = d
cnt = dict()
for i in [2,3,5]:
    cnt[i] = 0
    while x%i == 0:
        x //= i
        cnt[i] += 1

if x != 1:
    print(0)
    exit()

@lru_cache(maxsize=10**9)
def solve(x,a,b,c):
    a = max(a,0)
    b = max(b,0)
    c = max(c,0)
    if a == b == c == 0:
        return 1
    if x == 0:
        return 0
    res = 0
    res += solve(x-1,a,b,c)
    res += solve(x-1,a-1,b,c)
    res += solve(x-1,a,b-1,c)
    res += solve(x-1,a-2,b,c)
    res += solve(x-1,a,b,c-1)
    res += solve(x-1,a-1,b-1,c)
    return res/6

ans = solve(n,cnt[2],cnt[3],cnt[5])
print(ans)