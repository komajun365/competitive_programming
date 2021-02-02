import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int, input().split())
a = list(map(int, input().split()))

#############

mod = 10**9 + 7
max = 10**5+10
fac, finv, inv = [0]*max, [0]*max, [0]*max

def comInit(max):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max)

# 二項係数の計算
def com(n,k):
    if(n < k):
        return 0
    if( n<0 | k < 0):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

#############

a = sorted(a)

mul = [0]* n
mul[k-1] = 1
for i in range(k, n):
    mul[i] = com(i, k-1)

ans = 0
for i in range(n):
    ans += (a[i] * mul[i]) - (a[i] * mul[ -1*(i+1)]) % mod
    ans = ans % mod

print(ans)
