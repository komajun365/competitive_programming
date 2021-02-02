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

import bisect

n = int(input())
a = list(map(int,input().split()))

inc_l = [0] * n
inc_r = [0] * n
dec_l = [0] * n
dec_r = [0] * n

for x,pm,cnt in zip([a,a,a[::-1],a[::-1]],[1,-1,1,-1],[inc_l,dec_l,inc_r,dec_r]):
    lis = [10**10] * n
    for i,xi in enumerate(x):
        xi *= pm
        ind = bisect.bisect_left(lis,xi)
        cnt[i] = ind
        lis[ind] = xi

inc_r = inc_r[::-1]
dec_r = dec_r[::-1]

ans = 0
for i in range(n):
    ans = max(ans, min(inc_l[i],inc_r[i]), min(dec_l[i],dec_r[i]))
print(ans)

print(inc_l)
print(inc_r)
print(dec_l)
print(dec_r)
