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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

h,w,n = map(int,readline().split())
rc = [(1,1)]
for i in range(n):
    r,c = map(int,readline().split())
    rc.append((r,c))
rc.sort(key = lambda x: sum(x)*-1)
mod = 10**9+7

max_n = 3 * 10**5
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

# 二項係数の計算
def com(n,k):
    if(n < k):
        return 0
    if( (n<0) | (k < 0)):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

dp = [0] * (n+2)
dp[0] = 1
for i in range(n+1):
    ri,ci = rc[i]
    dp[i+1] = com(h+w-ri-ci,h-ri)
    for j in range(i):
        rj,cj = rc[j]
        if(ri<=rj)&(ci<=cj):
            dp[i+1] -= com(rj+cj-ri-ci,rj-ri) * dp[j+1]
            dp[i+1] %= mod

print(dp[-1])

'''

ゴールに近い方から壁に順番を付ける
dp[i] = i番目の壁から、他の壁を通らずにゴールにたどり着く経路の数とする。
できそうでしょ？

'''
