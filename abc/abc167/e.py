# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m,k = map(int,input().split())
mod =  998244353

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = 3 * 10**5
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


ans = 0
color = pow((m-1), (n-k-1), mod)
color = (color*m) % mod
for i in range(k,-1,-1):
    tmp = color * com(n-1, i)
    tmp %= mod
    ans += tmp
    color *= (m-1)
    color %= mod

ans %= mod
print(ans)
