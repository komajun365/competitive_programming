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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m = map(int,readline().split())
s = [list(map(int,i.split())) for i in readlines()]
mod = 1_000_000_007

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = 10**6 + 10**4
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

for i in range(n):
    s[i].append(0)

s.append([0]*(m+1))

ans = 0
for i in range(n+1):
    for j in range(m+1):
        if(i==n)&(j==m):
            continue
        if(s[i][j] > 0):
            move = i+j+s[i][j]-1
            tmp = com(move,i) * com(move-i,j)
            tmp %= mod
            ans += tmp

        #飛び降り
        if(i!=0):
            if(s[i-1][j] - s[i][j] > 0):
                tmp = com(i-1+j+s[i-1][j], s[i-1][j]-1)
                tmp -= com(i-1+j+s[i][j], s[i][j]-1)
                tmp %= mod
                tmp *= com(i-1+j,j)
                tmp %= mod
                ans += tmp
        if(j!=0):
            if(s[i][j-1] - s[i][j] > 0):
                tmp = com(i+j-1+s[i][j-1], s[i][j-1]-1)
                tmp -= com(i+j-1+s[i][j], s[i][j]-1)
                tmp %= mod
                tmp *= com(i+j-1,i)
                tmp %= mod
                ans += tmp

        ans %= mod
        # print(i,j,ans)

print(ans)
