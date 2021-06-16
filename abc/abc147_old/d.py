# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int,input().split()))

mod = 10**9 + 7
bit_num = [0] * 60
bit_0 = [0] * 60
bit_1 = [0] * 60
for i in a:
    for j in range(60):
        if( (i>>j)&1 == 1 ):
            bit_num[j] += bit_0[j]
            bit_1[j] += 1
        else:
            bit_num[j] += bit_1[j]
            bit_0[j] += 1

ans = 0
for i in bit_num[::-1]:
    ans *= 2
    ans += i
    ans %= mod

print(ans)
