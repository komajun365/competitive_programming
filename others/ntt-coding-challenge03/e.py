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

import itertools

k = int(input())

ntt = []

for i in range(1,6):
    base = 0
    for j in range(i*3):
        base = base*10 + 1
    for c in itertools.combinations(range(i*3), i):
        base_a = 0
        for ci in c:
            base_a += 10**ci
        base_b = base- base_a
        if(base_a < base_b):
            base_a,base_b = base_b,base_a
        for a in range(1,10):
            for b in range(0,10):
                if(a==b):
                    continue
                ntt.append(base_a*a + base_b*b)
    if(len(ntt) >= k):
        break

ntt.sort()
print(ntt[k-1])




'''
全部作ればいいやマインド
'''
