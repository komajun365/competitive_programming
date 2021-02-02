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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

from numba import njit,prange

# @njit
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

primes = sieve(10**7)
p_set = set(primes)

# @njit
def l_count(a,b):
    l = 0
    while(True):
        num = l**2 + a*l + b
        if(num in p_set):
            l += 1
        else:
            break
    return l

# @njit(parallel=True)
def calc():
    max_l = 0
    ans = [0,0]
    for i in range(2001):
        if(i%100==0):
            print(i)
        i -= 1000
        for j in primes:
            if(j > 1000):
                break
            l_ij = l_count(i,j)
            if( max_l < l_ij):
                max_l = l_ij
                ans = [i,j]

    print(max_l)
    print(ans)
    print(ans[0]*ans[1])

calc()



'''
-1000<=a<=1000
0<b<=1000 (bは素数)
これで全探索しましょう。

最長で仮に1000個生成できたとして
10**7ぐらいまでの素数を持っておけば問題なさそう。

numbaの練習もかねて。

'''
