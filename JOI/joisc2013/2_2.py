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

r,c,n,*ab = map(int,read().split())
mod = 10**9+7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = 3 * 10**3 + 10
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

a_min = r
a_max = 1
b_min = c
b_max = 1
it = iter(ab)
for a,b in zip(it,it):
    a_min = min(a_min,a)
    a_max = max(a_max,a)
    b_min = min(b_min,b)
    b_max = max(b_max,b)

h0 = (a_max-a_min+1)
w0 = (b_max-b_min+1)
rem = h0*w0 - n
ans1 = 1
for i in range(1,rem+1):
    ans1 *= i
    ans1 %= mod

dp =[[0] * (c+1) for _ in range(r+1)]
dp[h0][w0] = ans1

for i in range(h0,r+1):
    for j in range(w0,c+1):
        if i != r:
            dp[i+1][j] += dp[i][j] * 2 * fac[j]
            dp[i+1][j] %= mod
        if j != c:
            dp[i][j+1] += dp[i][j] * 2 * fac[i]
            dp[i][j+1] %= mod

ans = dp[-1][-1]
ans *= com(r-h0, r-a_max)
ans %= mod
ans *= com(c-w0, c-b_max)

inv2 = pow(2,mod-2,mod)
ans *= pow(inv2, r-h0, mod)
ans %= mod
ans *= pow(inv2, c-w0, mod)
ans %= mod

print(ans)

'''
step1
最初の長方形を作る
マスコット初期値の最小・最大のx/yの値を持ってきて、
空きマスを埋めればいい

step2
左右、上下に長方形を拡大していく。
(a,b) -> (r,c)まで

(a,b) -> (a,b+1)に拡大するとき

dp[a][b+1] = 2 * dp[a][b] * a!

ただ、上下左右に自由に伸ばしていくと、元のマスにおさまるかどうかは確率ゲーになる。
上下に伸ばした試行回数がh回、上にu回下にd回のばしていればOKの時、
上下がうまくいっている確率は com(h,u)/2**h

左右も同じ。

'''
