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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

h,w = list(map(int,readline().split()))
data = list(map(int,read().split()))
a = data[:h*w]
q = data[h*w]
rc = data[h*w+1:]
mod = 10**9+7

cnt0 = 0
tot = 1
cnt0_h = [0]*h
cnt0_w = [0]*w
tot_h = [1]*h
tot_w = [1]*w
for i in range(h):
    for j in range(w):
        aij = a[i*w+j]
        if(aij==0):
            cnt0 += 1
            cnt0_h[i] += 1
            cnt0_w[j] += 1
        else:
            tot *= aij
            tot %= mod
            tot_h[i] *= aij
            tot_h[i] %= mod
            tot_w[j] *= aij
            tot_w[j] %= mod

ans =[]
it = iter(rc)
for r,c in zip(it,it):
    r -= 1
    c -= 1
    num0 = cnt0 - cnt0_h[r] - cnt0_w[c] + (a[r*w+c]==0)
    if(num0>0):
        ans.append(0)
        continue
    ans_i = tot * pow(tot_h[r],mod-2,mod) * pow(tot_w[c],mod-2,mod)
    ans_i %= mod
    if(a[r*w+c] != 0):
        ans_i *= a[r*w+c]
        ans_i %= mod
    ans.append(ans_i)

print('\n'.join(map(str,ans)))

# print(cnt0)
# print(cnt0_h)
# print(cnt0_w)
