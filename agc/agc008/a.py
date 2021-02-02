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

x,y = map(int,input().split())
ans = abs(abs(x) - abs(y))
if(x*y>0)&(x>y):
    ans += 2
if(x*y < 0):
    ans += 1
if(x*y==0)&(x>y):
    ans += 1
print(ans)
