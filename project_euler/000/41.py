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
for i in [4,7]:
    for p in itertools.permutations(list(range(1,i+1))):
        x = 0
        for pi in p:
            x = x*10 + pi
        
        for y in range(2,x):
            if y**2 > x:
                ans = max(ans,x)
                break
            if x % y == 0:
                break

print(ans)














