# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
mod = 10**9 + 7

ans = 0
for i in range(k,n+2):
    ans += i*(n-i+1) + 1
    ans %= mod
print(ans)
