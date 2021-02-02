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

s = input()
mod = 10**9+7

n = len(s)
rem = dict()
ans = n* pow(2,n-1,mod)
ans %= mod
for i,si in enumerate(s):
    if(not si in rem):
        rem[si] = 0
    ans -= rem[si] * pow(2,n-i-1,mod)
    ans %= mod
    rem[si] += pow(2,i,mod)
    rem[si] %= mod
print(ans)

# n = len(s)
# ans = 0
# cnt = dict()
# for si in s:
#     if(si in cnt):
#         cnt[si] += 1
#     else:
#         cnt[si] = 1
#     ans += pow(2,n-cnt[si],mod)
#     ans %= mod
# print(ans)

# n = len(s)
# ans = 0
# pos = dict()
# for i,si in enumerate(s):
#     if(si in pos):
#         left = i-pos[si]
#     else:
#         left = i
#     pos[si] = i
#
#     ans += left*(n-i)
#     ans %= mod
# print(ans)


# ans = 0
# now = 0
# bef = '?'
# for i,si in enumerate(s,1):
#     if(bef==si):
#         now += 1
#     else:
#         now += i
#     now %= mod
#     ans += now
#     ans %= mod
#     bef = si
# print(ans)
