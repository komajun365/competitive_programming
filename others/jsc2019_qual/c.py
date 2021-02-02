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
s = input()
mod = 10**9+7

ans = 1
p = 0
m = 0
for si in s:
    if((p-m)%2==0):
        if(si=='B'):
            p += 1
        else:
            ans *= (p-m)
            ans %= mod
            m += 1
    else:
        if(si=='W'):
            p += 1
        else:
            ans *= (p-m)
            ans %= mod
            m += 1

if(p!=m):
    ans = 0

for i in range(1,n+1):
    ans *= i
    ans %= mod

print(ans)
