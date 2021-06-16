import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,a,b = map(int, input().split())

mod = 10**9 + 7

ans = pow(2, n, mod) - 1
for i in [a,b]:
    child = 1
    mother = 1
    for j in range(1,i+1):
        child = child * (n-j + 1) % mod
        mother = mother * j % mod
    mother = pow(mother, mod-2, mod)
    ans -= (child * mother)%mod


ans = ans % mod

print(ans)
