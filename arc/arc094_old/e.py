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
data = list(map(int,read().split()))

tot = 0
same = 0
min_b = 10**9
it = iter(data)
for a,b in zip(it,it):
    tot += a
    if(a==b):
        same += 1
    elif(a > b):
        min_b = min(min_b,b)

if(same==n):
    print(0)
else:
    print(tot-min_b)
