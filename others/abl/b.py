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

a,b,c,d = map(int,input().split())
if(a <= c <= b)|(a <= d <= b)|(c <= a <= d)|(c <= b <= d):
    print('Yes')
else:
    print('No')
