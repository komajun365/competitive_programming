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
'''
n = 4*10**7
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

primes = sieve(n)

from functools import lru_cache

@lru_cache(maxsize=4*10**7)
def get_length(x):
    if(x==1):
        return 1

    return 1 + get_length(phi(x))

@lru_cache(maxsize=4*10**7)
def phi(x):
    res = x
    x2 = x
    for i in primes:
        if(x2%i==0):
            res = res*(i-1)//i
            while(x2%i==0):
                x2 //= i
        if(i**2 > x2):
            break
    if(x2!=1):
        res = res*(x2-1)//x2
    print(x,res)
    return res

ans = 0
for ind,i in enumerate(primes[:10]):
    if(ind%10**6 == 0):
        print(ind,i)
    if(get_length(i)==25):
        ans += i

print(ans)
# print(len(primes))
