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

w,h,n,*sk = map(int,read().split())
s_set = set()
k_set = set()
for si in sk[::2]:
    s_set.add(si)
for ki in sk[1::2]:
    k_set.add(ki)

ans = w*h - (w-len(s_set))*(h-len(k_set)) - n
print(ans)
