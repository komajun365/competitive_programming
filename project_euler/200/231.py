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

n = 2 * 10**7
k = 15 * 10**6
def sieve(n):
    if( n <= 1):
        return []
    elif(n==2):
        return [2]

    primes = [2]
    primes_append = primes.append
    len_list = (n+1)//2
    flags = [True] * len_list
    flags[0] = False
    for i in range(len_list):
        if(flags[i]):
            primes_append(i*2+1)
            start = ((i*2+1)**2)//2
            for j in range( start, len_list, i*2+1):
                flags[j] = False
    return primes

primes = sieve(n)

def count_fac(n,x):
    res = 0
    while(n>0):
        n //= x
        res += n
    return res

ans = 0
for i in primes:
    cnt = count_fac(n,i) - count_fac(k,i) - count_fac(n-k,i)
    ans += i*cnt

print(ans)




'''
素因数の数を管理すれば勝ち。

'''
