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
f = open('p042_words.txt', 'r')
sys.stdin = f

import itertools

ans = 0
for p in itertools.permutations(list(range(10))):
    p = list(p)
    if p[0] == 0:
        continue
    if p[3] % 2 == 1:
        continue
    for i,d in zip([2,3,4,5,6,7],[3,5,7,11,13,17]):
        x = 0
        for j in range(i,i+3):
            x = x*10 + p[j]
        if x % d != 0:
            break
    else:
        x = 0
        for pi in p:
            x = x*10 + pi
        ans = ans + x
        print(x)

print(ans)















