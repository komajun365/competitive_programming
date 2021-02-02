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

num_st = n-m

# dp1 = [0] * (l+1)
# for i in range(l+1):
#     dp1[i] = [[0] * (n+1) for _ in range(num_st+1)]

# dp1[0][0][0] = 1
# for i in range(l):
#     for j in range(num_st+1):
#         for k in range(n+1):


dp1 = [[0] * (n+1) for _ in range(num_st+1)]
dp1[0][0] = 1
for k in range(1,l+1):
    tmp = [[0] * (n+1) for _ in range(num_st+1)]
    for i in range(num_st+1):
        for j in range(n+1):
            i2,j2 = i,j
            x = dp1[i][j]
            cnt = 0
            while(i2 <= num_st)&(j2 <= n):
                tmp[i2][j2] += x
                tmp[i2][j2] %= mod
                i2 += 1
                j2 += k
                cnt += 1
                x *= inv[cnt]
                x %= mod
                if(k > 1):
                    x *= inv[2]
                    x %= mod
    dp1,tmp = tmp,dp1

dp1_b = tmp


# dp2 = [[0] * (n+1) for _ in range(l+1)]
# dp2[0][0] = 1
# for i in range(1,l+1):
#     for j in range(1,n+1):
#         if(j>=i):
#             dp2[i][j] = (i*dp2[i][j-1] + dp2[i-1][j-1])%mod

# bn = []
# bn_b = []
# for j in range(n+1):
#     tot = 0
#     for i in range(l):
#         tot += dp2[i][j]
#     tot %= mod
#     bn_b.append(tot)
#     tot = (tot + dp2[-1][j])%mod
#     bn.append(tot)

# dp2 = [0] * (l+1)
# for i in range(l+1):
#     dp2[i] = [[0] * (n+1) for _ in range(n+1)]
# dp2[1][1][1] = 1
# for k in range(l+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if(j <= i):
#                 if(j > 0):
#                     dp2[k][i][j] += dp2[k][i-1][j-1]
#                 if(k > 0):
#                     dp2[k][i][j] += j * dp2[k-1][i-1][j]
#                 dp2[k][i][j] %= mod

# bn = []
# bn_b = []
# for i in range(n+1):
#     tot = 0
#     for j in range(n+1):
#         for k in range(l):
#             tot += dp2[k][i][j]
#         tot %= mod
#     bn_b.append(tot)
#     for j in range(n+1):
#         tot += dp2[-1][i][j]
#         tot %= mod 
#     bn.append(tot)

dp2 = [[0] * (n+1) for _ in range(l+1)]
dp2[0][0] = 1
dp2[1][0] = 1
for i in range(1,l):
    for j in range(n+1):
        for k in range(n+1):
            j2 = j + (i+1) * k
            if(j2 > n):
                break
            dp2[i+1][j2] += dp2[i][j] * com(j2,j) * fac[j2-j] * pow(finv[i+1],k,mod) * finv[k]
            dp2[i+1][j2] %= mod




ans = 0
ans_b = 0
for i in range(n+1):
    ans += dp1[num_st][i] * fac[n] * finv[n-i] * dp2[-1][n-i]
    ans %= mod
    ans_b += dp1_b[num_st][i] * fac[n] * finv[n-i] * dp2[-2][n-i]
    ans_b %= mod

ans -= ans_b
ans %= mod

print(ans)

print(dp1)
print(dp1_b)
print(dp2)

# for i in dp2[:3]:
#     print(i)