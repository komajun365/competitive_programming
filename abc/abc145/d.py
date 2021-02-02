# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

x,y = map(int,input().split())
if((x+y)%3 != 0):
    print(0)
    exit()

if(abs(y-x) > min(x,y)):
    print(0)
    exit()

sum_ = (x+y)//3
right = y - sum_
up = x - sum_

mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = 10**6 + 10
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

ans = com((right+up), right)
print(ans)
