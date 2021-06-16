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
f = open('p042_words.txt', 'r')
sys.stdin = f

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

import itertools

primes = set(sieve(9999))

for d in range(1,5000):
    for x1 in range(1001,10000,2):
        x2 = x1 + d
        x3 = x2 + d
        if x3 >= 10000:
            continue
        if x1 in primes and x2 in primes and x3 in primes:
            s1 = sorted(str(x1))
            s2 = sorted(str(x2))
            s3 = sorted(str(x3))
            if s1 == s2 == s3:
                print(x1,x2,x3)
                print(s1+s2+s3)





















