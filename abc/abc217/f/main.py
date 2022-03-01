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

import sys
read = sys.stdin.buffer.read

n,m,*ab = map(int,read().split())
mod = 998244353
n2 = n*2

max_n = n*2 + 10
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

like = [[0] * (n2) for _ in range(n2)]
it = iter(ab)
for a,b in zip(it,it):
    like[a-1][b-1] = 1
    like[b-1][a-1] = 1

dp = [[0] * (n2+1) for _ in range(n2+1)]
for i in range(n2+1):
    dp[i][i] = 1

for i in range(2,n2+1,2):
    for l in range(n2-i+1):
        for r in range(l+1, l+i,2):
            if like[l][r] == 0:
                continue
            dp[l][l+i] += dp[l+1][r] * dp[r+1][l+i] * com(i//2, (r-l+1)//2)
            dp[l][l+i] %= mod

print(dp[0][-1])

# for i in dp:
#     print(i)