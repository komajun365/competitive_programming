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

n,m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
mod = 10**9 + 7

uni_x = 0
for i in range(1,n):
    uni_x += i * (n-i) * (x[i]-x[i-1])
    uni_x %= mod

ans = 0
for i in range(1,m):
    ans += i * (m-i) * (y[i]-y[i-1])
    ans %= mod

ans *= uni_x
ans %= mod

print(ans)


'''
10

1*9+2*8+3*7+4*6+5*5+
9,16,


'''
