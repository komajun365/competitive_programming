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

from math import gcd
from collections import defaultdict

n,m = map(int,input().split())
s = input()
t = input()

ans = n*m // gcd(n,m)
d = defaultdict(lambda : '?')

for i,si in enumerate(s):
    d[i * ans//n] = si

for j,tj in enumerate(t):
    if(not d[j * ans//m] in ['?', tj]):
        print(-1)
        exit()

print(ans)
