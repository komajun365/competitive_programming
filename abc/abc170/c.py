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

x,n = map(int,input().split())
if(n==0):
    print(x)
    exit()

p = set(map(int,input().split()))

ans = -2
dif = 1000
for i in range(-1,102):
    if(i in p):
        continue
    dif_i = abs(i-x)
    if(dif > dif_i):
        dif = dif_i
        ans = i

print(ans)
