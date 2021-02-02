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

n = int(input())
a = [0] + list(map(int,input().split()))

cnt = 0
for i in range(n,0,-1):
    ai = a[i]
    if(ai > i):
        print('No')
        exit()
    ai += cnt
    if(ai % i != 0):
        print('No')
        exit()
    cnt += ai//i

print('Yes')
