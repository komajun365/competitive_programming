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

# import itertools

p,k = map(int,input().split())
mod = 10**9+7

ans = (pow(10,p-1,mod)-1) * pow(p,mod-2,mod)
ans = (ans + (k==0))%mod
print(ans)

# p = 17
# pr = itertools.product(range(10), repeat=p-1)
# cnt = [0]*p
# for a in pr:
#     tmp = 0
#     for i,ai in enumerate(a,1):
#         tmp += i*ai
#     cnt[tmp%p] += 1
#
# print(cnt)
# print(pow(10,p-1,p))
