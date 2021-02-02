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

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

h,w,*s = read().split()
h = int(h)
w = int(w)
mod = 10**9+7

n = 0
for si in s:
    n += si.count('.')

lamps = [[-1] * w for _ in range(h)]
for i in range(h):
    l = 0
    si = s[i]
    for j in range(w):
        if(si[j] == '#'):
            num = j-l
            for k in range(l,j):
                lamps[i][k] += num
            l = j+1
    if(l != w):
        for k in range(l,w):
            lamps[i][k] += w-l

for j in range(w):
    l = 0
    for i in range(h):
        if(s[i][j] == '#'):
            num = i-l
            for k in range(l,i):
                lamps[k][j] += num
            l = i+1
    if(l != h):
        for k in range(l,h):
            lamps[k][j] += h-l

cnt = [0] * (h+w)
for i in range(h):
    for j in range(w):
        if(lamps[i][j] != -1):
            cnt[lamps[i][j]] += 1


ans = 0
for i,ci in enumerate(cnt):
    if(n-i < 0):
        break
    ans += ci * pow(2,n-i,mod) * (pow(2,i,mod) - 1)
    ans %= mod
print(ans)
