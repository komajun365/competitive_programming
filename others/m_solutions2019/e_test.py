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

q = int(readline())
xdn = list(map(int,read().split()))
mod = 1_000_003

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = mod + 10
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

def prod(l,r):
    #lからr-1までの累積
    res = (fac[r-1] * finv[l-1])%mod
    return res

def solve(x,d,n):
    if(d==0):
        return pow(x,n,mod)
    x0 = (x * inv[d])%mod
    xn = x0 + n
    if(xn > mod)|(x0==0):
        return 0
    res = (prod(x0,xn) * pow(d,n,mod))%mod
    return res


def solve2(x,d,n):
    res = 1
    for i in range(n):
        res *= x + i*d
        res %= mod

    return res

import random
for _ in range(100000):
    x = random.randint(0,1000002)
    d = random.randint(0,1000002)
    n = random.randint(1,100)

    res1 = solve(x,d,n)
    res2 = solve2(x,d,n)
    if(res1 != res2 ):
        print(x,d,n)
        print(res1,res2)
        exit()






'''
1*2*3*4 = 4*8*12*16//(4**4)

(x,d,n) = (5,2,4)
5*7*9*11 = 500004*500005*500006*500007 * (2**4)

'''
