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

import itertools

def sieve(n):
    if( n <= 1):
        return []
    elif(n==2):
        return [2]

    primes = [2]
    len_list = (n+1)//2
    len_sqrt = int(len_list**0.5) + 1
    flags = [True] * len_list
    flags[0] = False
    for i in range(len_sqrt):
        if(flags[i]):
            start = ((i*2+1)**2)//2
            for j in range( start, len_list, i*2+1):
                flags[j] = False
    return [2] + [i*2+1 for i in range(len_list) if flags[i]]

primes = sieve(10**6)

def count(x):
    fac = []
    now = x
    for i in primes:
        if(i**2 > now):
            break
        if(now%i==0):
            fac.append(i)
            while(now%i==0):
                now //= i
    if(now!=1):
        fac.append(now)

    len_f = len(fac)
    res = 0
    for i in itertools.product([0,1],repeat=len_f):
        div = 1
        for ind,j in enumerate(i):
            if(j==1):
                div *= fac[ind]
        if(sum(i) %2==0):
            res += x//div
        else:
            res -= x//div

    return res




# x = 1
# for i in range(20):
#     x *= primes[i]
#     chi = count(x)
#     if(chi * 94744 < 15499 *x):
#         print(0,i,x)
#     if( chi * 94744 < 15499 * (x-1)):
#         print(1,i,x)
#         exit()

x0 = 223092870
for i in range(1,50):
    x = x0*i
    chi = count(x)
    if(chi * 94744 < 15499 * (x-1)):
        print(0,i,x)
        break



'''
dと素な数字の個数がわかればよい。

あらかじめ素数のリストを作っておき、
d%p==0　なら　エラストテネスの篩のような処理をする。
一つの数についてO(N*logN*√N)って感じ？
ちょっと重いですね。。。

√N以下の割り切れる素数をまず確認する。
あとは包除原理をつかえば、ほぼO(1)で計算できる

これならO(N√N)ぐらいか？

x = 60 = 2 * 3* 5

60 - (30+20+12) + (10+6+4) - 2 = 16
1,7,11,13,17,19,23,29
あってる。



'''
