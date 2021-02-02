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

n,q = map(int,readline().split())
c = list(map(int,readline().split()))
lr = list(map(int,read().split()))
it = iter(lr)
lr2 = []
for i,l,r in zip(range(q),it,it):
    lr2.append((r-1,l-1,i))

rem = [0] * (n+1)
before = [-1] * (n+1)
for i,ci in enumrate(c,1):
    rem[i] = rem[i-1]
    if(before[ci] != -1):


lr2.sort()
st = Seg_sum([1]*(n+1))
ans = [0] * q
before = [-1] * (n+1)
c_ind = 0
