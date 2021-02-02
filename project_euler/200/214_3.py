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

'''
素数列挙＆再帰関数でいけるかしら

φ(n)の求め方
素因数分解して、
a**x * b**y * c**z
φ(n) = (a**(x-1)-(a-1))*(b**(y-1)*(b-1))*(c**z-z)
 = n*(a-1)*(b-1)*(c-1)//(a*b*c)

素因数がわかれば計算できる！
とはいえ、最大でO(10*5)くらいはありそうですけれども・・・
ひとまずやってみましょう。

=====

きつかったです。
下からφ(x)を作っていきましょう。

φ(x)=yだっととします。
φ(2x)=y'は？
・x%2==0の場合
y' = 2y
・x%2==1の場合
y' = y

φ(3x)=y'は？
・x%3==0の場合
y' = 3y
・x%3!=0の場合
y' = 2y

'''
n = 4*10**7
# n = 100

def sieve_fac(n):
    if( n <= 1):
        return []
    elif(n==2):
        return [2]

    primes = []
    primes_append = primes.append
    len_list = (n+1)
    flags = [0] * len_list
    flags[0] = 1
    flags[1] = 1
    for i in range(len_list):
        if(flags[i] == 0):
            primes.append(i)
            for j in range( i, len_list, i):
                flags[j] = i
    return flags,primes

facs,primes = sieve_fac(n)
# print(facs[:20])


phi = [0] * (n+1)
phi[1] = 1

def calc_phi(x):
    if(phi[x] != 0):
        return phi[x]

    if(x == facs[x]):
        phi[x] = x-1
        return x-1

    i = facs[x]
    if(x%(i*i)!=0):
        phi[x] = calc_phi(x//i) * (i-1)
    else:
        phi[x] = calc_phi(x//i) * i
    return phi[x]

phi_len = [0] * (n+1)
phi_len[1] = 1
for i in range(2,n+1):
    if(i%(10**6)==0):
        print(i)
    phi_len[i] = 1 + phi_len[calc_phi(i)]

ans = 0
for i in primes:
    if(phi_len[i] == 25):
        ans += i

print(ans)
