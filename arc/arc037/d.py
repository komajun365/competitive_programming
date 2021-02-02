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

l = int(input())
mod = 10**9+7

s = [0]*(l+1)
t = [0]*(l+1)
u = [0]*(l+1)
s[0] = 1
t[0] = 2
u[0] = 1
for i in range(1,l+1):
    s[i] = s[i-1]*3 + pow(t[i-1],3,mod)
    s[i] %= mod
    t[i] = t[i-1] * (t[i-1] + pow(t[i-1],2,mod) - pow(u[i-1],2,mod))
    t[i] %= mod
    u[i] = u[i-1] * pow(t[i-1],2,mod) - pow(u[i-1],3,mod)
    u[i] %= mod

print(s[-1])
# print(s)
# print(t)
# print(u)
