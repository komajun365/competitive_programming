# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

# 解説ACする

n,k = map(int,input().split())
a = list(map(int,input().split()))
mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = 10**4
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

dp = [0] * (n+1)
dp[0] = fac[n]
for i in range(k):
    dp2 = [0] * (n+1)
    for j in range(n+1):
        for x in range(a[i]+1):
            if j + x > n:
                break
            dp2[j+x] += (dp[j] * com(n-x, a[i]-x) % mod) * finv[x]
            dp2[j+x] %= mod
    dp,dp2 = dp2,dp

ans = dp[-1]
print(ans)


