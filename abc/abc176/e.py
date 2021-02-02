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
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from heapq import heappop,heappush

H,W,M = map(int,readline().split())
hw = list(map(int,read().split()))

x_num = [0] * (H+1)
y_num = [0] * (W+1)

it = iter(hw)
for h,w in zip(it,it):
    x_num[h] += 1
    y_num[w] += 1

x_max = max(x_num)
y_max = max(y_num)

x_max_set = set()
y_max_set = set()
for i,num in enumerate(x_num):
    if(num == x_max):
        x_max_set.add(i)

for i,num in enumerate(y_num):
    if(num == y_max):
        y_max_set.add(i)

cnt = 0
it = iter(hw)
for h,w in zip(it,it):
    if(h in x_max_set)&(w in y_max_set):
        cnt += 1

point = len(x_max_set) * len(y_max_set)
ans = x_max+y_max
if(point == cnt):
    ans -= 1
print(ans)
