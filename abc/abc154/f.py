import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

r1, c1, r2, c2 = map(int, input().split())

#############

mod = 10**9 + 7
max = 3 * 10**6
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
    if( (n<0) | (k < 0)):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

#############
ans = (com(r2+c2+2,r2+1) - com(r2+c1+1, c1) - com(r1+c2+1, r1) + com(r1+c1, r1)) % mod

print(ans)
