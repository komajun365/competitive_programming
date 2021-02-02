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
a = list(map(int,input().split()))
mod = 10**9+7

max_n = n+1
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

cumsum_l = [0] * (n+1)
cumsum_r = [0] * (n+1)
for i in range(n):
    cumsum_l[i] = (cumsum_l[i-1] + a[i])%mod
for i in range(n-1,-1,-1):
    cumsum_r[i] = (cumsum_r[i+1] + a[i])%mod

ans = cumsum_r[0] * fac[n]
ans %= mod

for i in range(1,n):
    tot = (cumsum_l[n-1-i] + cumsum_r[i])%mod
    ans += tot * fac[n] * inv[i+1]
    ans %= mod
print(ans)



'''
i番目のブロックについて、
i+j番目のブロックを取り除くときにどう寄与するか？

i,i+1,...i+jのなかで、i+jが一番最初に取り除かれるときだけ寄与する。

n個を(j+1)と（n-j-i）に分ける
j! * (n-j-1)!の並び替え
→　com(n,j+1) * j! * (n-j-1)!



'''
