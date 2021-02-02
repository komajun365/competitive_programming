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

k = int(input())
s = input()
n = len(s)

mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = 2 * 10**6 + 100
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
ex25 = [1] * (k+1)
ex26 = [1] * (k+1)
for i in range(1,k+1):
    ex25[i] = (ex25[i-1] * 25)%mod
    ex26[i] = (ex26[i-1] * 26)%mod

for i in range(k+1):
    j = k-i
    tmp = ex25[i] * com(n+i-1,i) * ex26[j]
    ans = (ans+tmp)%mod

print(ans)
