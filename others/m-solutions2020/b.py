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

a,b,c = map(int,input().split())
k = int(input())

cnt = 0
while(b<=a):
    cnt += 1
    b *= 2
while(c<=b):
    cnt += 1
    c *= 2

if(cnt <= k):
    print('Yes')
else:
    print('No')
