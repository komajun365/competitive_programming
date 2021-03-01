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

from collections import defaultdict
mod = 998244353

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = 3 * 10**5 + 100
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

n,a,b,k = map(int,input().split())

red = defaultdict(int)
for i in range(n+1):
    red[i*a] = com(n,i)

ans = 0
for i in range(n+1):
    point = k - b*i
    if(point < 0):
        break
    ans += red[point] * com(n,i)
    ans %= mod

print(ans)



'''
赤だけ考える
合計がAx点になるような塗り方はnCxで求まる

青だけ考える
合計がBy点になるような塗り方はnCyで求まる

解けました。


'''
