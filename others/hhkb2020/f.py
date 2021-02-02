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

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n,*lr = map(int,read().split())
mod = 10**9 + 7

max_n = n+10
fac, finv, inv = [0]*max_n, [0]*max_n, [0]*max_n

def comInit(max_n):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max_n):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max_n)

it = iter(lr)
lr2 = [ [l,r] for l,r in zip(it,it) ]
q = []
for i in range(n):
    l,r = lr2[i]
    q.append([l,i,0])
    q.append([r,i,1])
q.sort()

use = 0
k = 0
mul = 1
ans = 0
for i in range(n*2-1):
    x,j,side = q[i]
    if(side == 0):
        use += 1
        k += 1
    else:
        k -= 1
        mul *= lr2[j][1] - lr2[j][0]
        mul %= mod
    if(use == n):
        y = q[i+1][0]
        dif = y-x
        if(dif==0):
            continue
        tmp = (x*(k+1) + k*dif)%mod
        tmp *= ((inv[k+1] * fac[n+1])%mod) * mul
        tmp *= pow(dif,k,mod)
        tmp %= mod
        ans += tmp
        ans %= mod
        print(tmp)
    print(x,j,side,mul,ans)

print(ans)
