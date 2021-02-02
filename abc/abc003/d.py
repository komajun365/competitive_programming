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

r,c = map(int,input().split())
x,y = map(int,input().split())
d,l = map(int,input().split())
mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = 1000
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

def calc(x,y,d,l):
    if(x<=0)|(y<=0):
        return 0
    if(x*y < d+l):
        return 0

    free = x*y
    #dの決め方
    res = com(free,d)
    free -= d
    #lの決め方
    res *= com(free,l)
    res %= mod

    return res

ans = calc(x,y,d,l)
ans -= calc(x-1,y,d,l)*2 + calc(x,y-1,d,l)*2
ans += calc(x-1,y-1,d,l)*4 + calc(x-2,y,d,l) + calc(x,y-2,d,l)
ans -= calc(x-2,y-1,d,l)*2 + calc(x-1,y-2,d,l)*2
ans += calc(x-2,y-2,d,l)

ans %= mod
ans *= (r-x+1) * (c-y+1)
ans %= mod

print(ans)

'''
100点は簡単。
101点は包除で行けるか？




'''
