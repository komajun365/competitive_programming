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

n,m = map(int,input().split())
mod = 998244353

#################################

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = n+2*m + 100
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


a = 0
for x in range(min(m,n)+1):
    if(3*m-x)%2==1:
        continue
    y = (3*m-x)//2
    a += com(n,x)*fac[y+n-1]*finv[y]*finv[n-1]
    a %= mod

b = fac[n-1+m-1] * finv[n-1] * finv[m-1] * n
b %= mod

ans = a-b
ans %= mod

print(ans)


'''
(6,0,0):5
(5,1,0):20
(4,2,0):20
(3,3,0):10
(4,1,1):30
(3,2,1):60
(2,2,2):10
(3,1,1,1):20
(2,2,1,1):30
(2,1,1,1,1):5

奇数の人をx人選ぶ
y=(3m-x)//2を配る
x+y = (3m+x)//2
(x<=m)のときx+y<=2m

'''
# a = fac[n-1+3*m] * finv[n-1] * finv[3*m]
# a %= mod
# b = fac[n-1+m-1] * finv[n-1] * finv[m-1] * n
# b %= mod
# c = 0
# for i in range(2*m+1,min(3*m,n)+1):
#     c += fac[3*m-1]*finv[i-1]*finv[3*m-i]*com(n,i)
#     c %= mod
#
# d = 0
# k = min(n,2*m)
# for i in range(m+1,k+1):
#     if(3*m-i)%2==1:
#         continue
#     l = (3*m-i)//2
#     d += com(n,i) * fac[n+l-1]*finv[l]*finv[n-1]
#     d %= mod
#
# ans = a-b-c-d
# ans %= mod
