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

from math import gcd

def calc_k(n,a):
    gcd_num = a[0]
    for ai in a[1:]:
        gcd_num = gcd(gcd_num,ai)

    if(gcd_num > 1):
        # print('not coprime')
        # exit()
        return 'not coprime'

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

    p_6 = set(sieve(10**6))
    p_3 = sieve(10**3)

    use = [0] * (10**6+1)

    for ai in a:
        if(ai==1):
            continue
        divs = []
        for p in p_3:
            if(ai%p==0):
                divs.append(p)
                while(ai%p==0):
                    ai//=p
        if(ai != 1):
            divs.append(ai)

        for di in divs:
            if(use[di] != 0):
                # print('setwise coprime')
                # exit()
                return 'setwise coprime'
            use[di] = 1

    # print('pairwise coprime')
    return 'pairwise coprime'

def calc_f(N,A):
    g_all = A[0]
    for a in A[1:]:
        g_all = gcd(g_all, a)

    if g_all > 1:
        # print('not coprime')
        # quit()
        return 'not coprime'

    def sieve(n):
        is_prime = [True for _ in range(n+1)]
        is_prime[0] = False
        for i in range(2, n+1):
            if is_prime[i-1]:
                j = 2 * i
                while j <= n:
                    is_prime[j-1] = False
                    j += i
        table = [ i for i in range(1, n+1) if is_prime[i-1]]
        return is_prime, table


    appeared = [False] * (10**6 + 1)
    primes = sieve(10**3)[1]
    for a in A:
        if a == 1:
            continue
        for p in primes:
            if a % p == 0:
                if appeared[p]:
                    # print('setwise coprime')
                    # quit()
                    return 'setwise coprime'
                appeared[p] = True
                while a % p == 0:
                    a //= p

        if a != 1:
            if appeared[a]:
                # print('setwize coprime')
                # quit()
                return 'setwize coprime'

            appeared[a] = True

    # print('pairwise coprime')
    return 'pairwise coprime'
