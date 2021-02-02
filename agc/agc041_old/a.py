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

n,a,b = map(int,input().split())
dif1 = abs(a-b)

if(dif1%2==0):
    print(dif1//2)
else:
    dif2 = (a-1) + (b-1) + 1
    dif3 = (n-a) + (n-b) + 1
    print(min(dif2//2,dif3//2))
