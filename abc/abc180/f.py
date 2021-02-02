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

n,m,l = map(int,input().split())
mod = 10**9 + 7

if(l==1):
    print(0)
    exit()

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = 310
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

def calc(n,m,l):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(m+1):
            dp[i][j] += dp[i-1][j]
            for k in range(2,l+1):
                if(i-k < 0) or (j-k+1 < 0):
                    break
                tmp = (dp[i-k][j-k+1] * com(n-(i-k)-1,k-1) )% mod
                tmp *= (fac[k] * inv[2])% mod
                dp[i][j] += tmp % mod
                dp[i][j] %= mod
                # dp[i][j] += (dp[i-k][j-k+1] * com(n-(i-k)-1,k-1) * fac[k] * inv[2] )% mod
            if(i-2 >= 0) and (j-2 >= 0) and (l>=2):
                dp[i][j] += (dp[i-2][j-2] * (n-(i-1)))% mod
            for k in range(3,l+1):
                if(i-k < 0) or (j-k < 0):
                    break
                tmp = (dp[i-k][j-k] * com(n-(i-k)-1,k-1) )% mod
                tmp *= (fac[k-1] * inv[2])% mod
                dp[i][j] += tmp % mod
                dp[i][j] %= mod
                # dp[i][j] += (dp[i-k][j-k] * com(n-(i-k)-1,k-1) * fac[k-1] * inv[2])% mod
            dp[i][j] %= mod
    return dp[-1][-1]

ans = calc(n,m,l) - calc(n,m,l-1)
ans %= mod
print(ans)
