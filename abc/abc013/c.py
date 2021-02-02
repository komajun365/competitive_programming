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

n,h = map(int,input().split())
a,b,c,d,e = map(int,input().split())

b += e
d += e
h -= n*e

if(h > 0):
    print(0)
    exit()

ans = a*n
need = 1-h
for i in range(n+1):
    cost = i*a
    rem = need - i*b
    eat_d = max(0, ((rem-1)//d + 1))
    if( eat_d > n-i):
        continue
    cost += eat_d*c
    ans = min(ans,cost)

print(ans)
