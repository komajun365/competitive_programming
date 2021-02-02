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
mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = 1 * 10**5 + 100
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

ind = [-1] * (1+n)
for i,ai in enumerate(a,1):
    if(ind[ai]==-1):
        ind[ai] = i
    else:
        left = ind[ai]
        right = i
        break

ans = [0] * (n+2)
for k in range(1,n+2):
    cnt = com(n-1,k) + com(n-1,k-1)*2 - com(n - (right-left),k-1)
    if(k >= 2):
        cnt += com(n-1,k-2)
    ans[k] = cnt%mod

print('\n'.join(map(str,ans[1:])))





'''

1個だけ2回出てくる数字がある。
これを何回使う？で数え上げできそう。

・2回使う
→　(n-1)C(k-2)
・1回使う
＝　左使う　＋　右使う　－　間を使わない
= 2 * (n-1)C(k-1) - (n - (right-left))C(k-1)

・0回使う
→　(n-1)C(k)


'''
