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

x,y,a,b = map(int,input().split())

ans = -1
while(a*x < x+b)&(x < y):
    x *= a
    ans += 1

if(x < y):
    ans += (y-x-1)//b
    ans += 1

print(ans)
