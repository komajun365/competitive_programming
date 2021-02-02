# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
x = tuple(map(int,input().split()))

mod = 10**9 + 7
mul_l = [1] * (n+1)
mul_r = [1] * (n+1)
for i in range(1,n+1):
    mul_l[i] = mul_l[i-1] * i % mod

for i in range(n-1,-1, -1):
    mul_r[i] = mul_r[i+1] * i % mod

ans = 0
right = x[-1]
for i in range(n-1):
    tmp = right - x[i]
    tmp = tmp * mul_l[i] * mul_r[i+2] % mod
    ans = (ans + tmp)% mod

print(ans)
# print(mul_l)
# print(mul_r)

####
#
# k -> k+1 (0-indexed)
# 1 kCk
# 2 kC(k-1)
#
# k-1 kC2
# k kC1
# k+1 kC0
#
#
# k= 5
# 1*5!
# 2*4!
# 3*3!
# 4*2!
# 5*1!
# 6*0!
# 120+48+18+8+5+6 = 205


# k= 6
# 1*6!
# 2*5!
# 3*4!
# 4*3!
# 5*2!
# 6*1!
# 7*0!

# 3.5* 2**5
#
# (k+2)//2 * 2**5
