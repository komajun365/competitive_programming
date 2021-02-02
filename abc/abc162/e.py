# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
mod = 10**9 + 7
count_gcd = [0]*(1+k)

ans = 0
for i in range(k,0,-1):
    tmp = pow(k//i, n, mod)
    for j in range(2, k//i + 1):
        tmp  =  (tmp - count_gcd[j*i])%mod
    count_gcd[i] = tmp
    ans = (ans +  tmp*i) % mod

print(ans)
