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

class fenwick_tree():
    def __init__(self, n:int, mod:int = 0):
        self.__mod = mod
        self.__n = n
        self.__data = [0] * self.__n

    def add(self, p:int, x:int):
        assert (0 <= p) & (p < self.__n)
        if(self.__mod == 0):
            self.__add_mod0(p,x)
        else:
            self.__add_mod(p,x)

    def __add_mod0(self, p:int, x:int):
        p+=1
        while( p<= self.__n):
            self.__data[p-1] += x
            p += p & -p

    def __add_mod(self, p:int, x:int):
        p+=1
        while( p<= self.__n):
            self.__data[p-1] += x
            self.__data[p-1] %= self.__mod
            p += p & -p

    def sum(self, l:int, r:int):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        if(self.__mod == 0):
            return self.__sum_mod0(r) - self.__sum_mod0(l)
        else:
            return self.__sum_mod(r) - self.__sum_mod(l)

    def __sum_mod0(self, r:int):
        s = 0
        while(r > 0):
            s += self.__data[r-1]
            r -= r & -r
        return s

    def __sum_mod(self, r:int):
        s = 0
        while(r > 0):
            s += self.__data[r-1]
            s %= self.__mod
            r -= r & -r
        return s

n = int(input())
a = list(map(int,input().split()))
mod = 998244353

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = 2 * 10**5 + 100
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

inverse = 0

a_ind = [[ai,i] for i,ai in enumerate(a)]
a_ind.sort(key= lambda x: -1*x[0]*10**6 - x[1])

d = {}
bit = fenwick_tree(n)
for ai,i in a_ind:
    inverse += bit.sum(0,i+1)
    bit.add(i,1)
    if(not ai in d):
        d[ai] = 1
    else:
        d[ai] += 1

inverse %= mod

inverse_all = n*(n-1)//2
for i in d.values():
    inverse_all -= i*(i-1)//2
inverse_all %= mod


combs = [1] * (n+1)
comb_l = [1] * (n+1)
comb_r = [1] * (n+2)
one = [0] * (n+1)
pair = [0] * (n+1)
for i in range(1,n+1):
    combs[i] = com(n,i)
    comb_l[i] = (comb_l[i-1] * combs[i])%mod
    one[i] = com(n-1,i-1)
    pair[i] = com(n-2,i-2)

for i in range(n,0,-1):
    comb_r[i] = (comb_r[i+1]*combs[i])%mod

ans = 0
ones = 0
for i in range(1,n+1):
    ans += ones * inverse_all * comb_r[i+1] * one[i]
    ans %= mod
    ones = (ones * combs[i] + comb_l[i-1] * one[i])%mod
    # print(i,ans)

    ans += pair[i] * inverse * comb_l[i-1] * comb_r[i+1]
    ans %= mod
    # print(i,ans)

print(ans)
# print(combs)
# print(comb_l)
# print(comb_r)
# print(one)
# print(pair)
