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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = list(map(int,readline().split()))
q = int(readline())
bc = list(map(int,read().split()))

from collections import defaultdict
d = defaultdict(int)

for i in a:
    d[i] += 1

ans = []
si = sum(a)
it = iter(bc)
for b,c in zip(it,it):
    d[c] += d[b]
    si += (c*d[b]) - b*d[b]
    d[b] = 0
    ans.append(si)

print('\n'.join(map(str,ans)))
