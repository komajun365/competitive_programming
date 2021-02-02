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

n,k = map(int,input().split())
mod = 1_777_777_777

# テーブルを作る(前処理)
max_n = k + 10
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

ans = 0
for i in range(2,k+1):
    ans += finv[i] * (1-2*(i%2))
    ans %= mod

ans *= fac[k]
ans %= mod

for i in range(k):
    ans *= (n-i)%mod
    ans %= mod
    ans *= inv[i+1]
    ans %= mod

print(ans)
# print(fac)
# print(finv)
