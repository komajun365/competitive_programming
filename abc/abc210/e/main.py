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
from math import gcd

n,m,*data = map(int,read().split())

it = iter(data)
ac = [[a,c] for a,c in zip(it,it)]
ac.sort(key=lambda x: x[1])

ans = 0
now = n
for a,c in ac:
    g = gcd(now, a)
    ans += c * (now - g)
    now = g
    if now == 1:
        print(ans)
        exit()

print(-1)