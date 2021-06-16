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
d = defaultdict(int)

n = int(input())
a = list(map(int,input().split()))

for ai in a:
    d[ai] += 1

ans = 0
for k,v in d.items():
    if(k > v):
        ans += v
    else:
        ans += (v-k)

print(ans)
