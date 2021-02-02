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
mod = 10**9 + 7

cnt = [0] * 26
for i in range(26):
    cnt[i] = s.count(chr(i+97)) + 1

ans = 1
for i in cnt:
    ans *= i
    ans %= mod

ans -= 1
ans %= mod
print(ans)


# ans = 0
# cnt = [1] * 26
# for i,ch in enumerate(s):
#     tmp = 1
#     for j in range(26):
#         if(j==(ord(ch) - 97)):
#             continue
#         tmp *= cnt[j]
#         tmp %= mod
#     ans += tmp
#     ans %= mod
#     cnt[ord(ch) - 97] += 1
#
# print(ans)
