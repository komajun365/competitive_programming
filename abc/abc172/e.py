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

n,m = map(int,input().split())
mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = 5 * 10**5 + 100
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

cnt = [0] * (n+1)
tot = 0
for i in range(n,-1,-1):
    cnt[i] = com(n,i)*(fac[n-i])*com(m-i ,n-i)
    cnt[i] %= mod
    tot = cnt[i] - tot
    tot %= mod

ans = tot * fac[m] * finv[m-n]
ans %= mod
print(ans)



'''
攪乱順列の計算式
1,...nを並び替えて、i番目がiでない数列の数anは
an = n! * Σ_{2<=k<=n}((-1)^k/k!)

らしい。
普通に包除原理で考えたいですね。


攪乱順列を数えた後に、
M!/(M-N!) を書けましょう。

'''
