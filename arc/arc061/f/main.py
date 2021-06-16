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

n,m,k = map(int,input().split())
mod = 10**9 + 7
tot = n+m+k

max_n = tot + 10
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

ans = 0
ex3 = [1] * (tot+1)
for i in range(tot):
    ex3[i+1] = ex3[i] * 3 % mod

ans = 0
com_num = 1
for i in range(m+k+1):
    tmp = com(n-1+i, i) * ex3[m+k-i] % mod
    tmp *= com_num
    tmp %= mod
    ans += tmp
    ans %= mod

    com_num *= 2
    if i >= m:
        com_num -= com(i,m)
    if i >= k:
        com_num -= com(i,k)
    com_num %= mod
    # print(i,ans,tmp,com_num)

print(ans)