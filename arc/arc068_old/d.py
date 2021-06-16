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

from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))

d = defaultdict(int)
for ai in a:
    d[ai] += 1

ans = 0
pair = 0
for k,v in d.items():
    if(v==0):
        continue
    if(v%2==1):
        ans += 1
    else:
        pair += 1

ans += 2*(pair//2)
print(ans)
