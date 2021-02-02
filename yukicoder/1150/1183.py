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
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = [ai^bi for ai,bi in zip(a,b) ]
for i in range(1,n):
    if(c[i]==c[i-1]==1):
        c[i-1] -= 1
print(sum(c))
