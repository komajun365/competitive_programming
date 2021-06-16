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

n,k = map(int,input().split())
a = list(map(int,input().split()))
mod = 998244353

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = 500
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

ans = [0] * (k+1)
ex = [1] * n
ex_sum = [n]
for i in range(1,k+1):
    for j in range(n):
        ex[j] *= a[j]
        ex[j] %= mod
    ex_sum.append( sum(ex) % mod )

    tmp = 0
    for j in range(i+1):
        tmp += ex_sum[j] * ex_sum[i-j] * com(i,j)
        tmp %= mod
    tmp -= ex_sum[-1] * pow(2,i,mod)
    tmp *= inv[2]
    tmp %= mod
    ans[i] = tmp

print('\n'.join(map(str,ans[1:])))
# print(ex_sum)

