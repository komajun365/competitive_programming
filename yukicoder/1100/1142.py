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

n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mod = 10**9+7

ax = [0]*1024
bx = [0]*1024
for xx,x in zip([ax,bx],[a,b]):
    tmp = 0
    # xx[0] += 1
    for xi in x:
        tmp = tmp^xi
        xx[tmp] += 1

ax2 = [ ai*2 for ai in ax]
bx2 = [ bi*2 for bi in bx]
for xx,xx2 in zip([ax,bx],[ax2,bx2]):
    for i in range(1024):
        for j in range(1024):
            if(i==j):
                xx2[0] += (xx[i]*(xx[i]-1))
                xx2[0] %= mod
            else:
                xx2[i ^ j] += xx[i]*xx[j]
                xx2[i ^ j] %= mod

ans = 0
for i in range(1024):
    ans += ax2[i] * bx2[k^i]
    ans %= mod
ans *= pow(4,mod-2,mod)
ans %= mod

print(ans)

print(ax[:10])
print(bx[:10])
print(ax2[:10])
print(bx2[:10])
