# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
mod = 10**9 + 7

dp = [[0] * 13 for _ in range(2)]
tmp = 0
for si in s:
    if(si != '?'):
        tmp = (tmp*10 + int(si)) % 13
    else:
        tmp = tmp*10 % 13

dp[0][tmp] = 1
exp10 = 1
pointer = 0
for i,si in enumerate(s[::-1]):

    if(si!='?'):
        exp10 = exp10 * 10 % 13
        continue

    pointer = 1 - pointer
    for j in range(13):
        dp[pointer][j] = 0

    for j in range(13):
        for k in range(10):
            dp[pointer][(j + exp10*k)%13] += dp[1-pointer][j]

    for j in range(13):
        dp[pointer][j] %= mod

    exp10 = exp10 * 10 % 13

print(dp[pointer][5])
