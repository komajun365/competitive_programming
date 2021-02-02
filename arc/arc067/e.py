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

n,a,b,c,d = map(int,input().split())
mod = 10**9 + 7

max = 2 * 10**3
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

dp = [[0] * (n+1) for _ in range(b+2)]

for i in range(a,b+1):
    dp[i][0] = 1
    for j in range(n+1):
        com_num = 1
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod
        for k in range(j+i,n+1,i):
            k_ind = (k-j)//i
            com_num *= com(n-k+i,i)
            com_num %= mod
            if(c <= k_ind <= d):
                dp[i+1][k] += dp[i][j] * com_num * finv[k_ind]
                dp[i+1][k] %= mod

print(dp[b+1][-1])

# print(dp)

'''
dp[i][j] := i-1人のグループまで作ることを考えて、j人までグループ入りしている場合の数

dp[i+1][j] += dp[i][j-i] * com()



'''
