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

n,z = map(int,input().split())
if(n>=3)|(z==1):
    print('No')
    exit()

x = 1
y = z-1
while(x<=y):
    zn = x**n + y**n
    if(zn == z**n):
        print('Yes')
        exit()
    elif(zn > z**n):
        y -= 1
    else:
        x += 1
print('No')
