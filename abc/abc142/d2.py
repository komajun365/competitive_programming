# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from fractions import gcd
a,b = map(int,input().split())

c = gcd(a,b)
if(c==1):
    print(1)
    exit()

max_n = int(c**(1/2))+1
#エラストテネスの篩
#n以下の素数のリストを返却
#2n+1だけ見る
def sieve(n):
    if( n <= 1):
        return []
    elif(n==2):
        return[2]

    primes = [2]
    len_list = (n+1)//2
    flags = [True] * len_list
    flags[0] = False
    for i in range(len_list):
        if(flags[i]):
            primes.append(i*2+1)
            for j in range( i*3+1, len_list, i*2+1):
                flags[j] = False
    return primes

primes = sieve(max_n)

nums = 1
prime_check = 1
for i in primes:
    if(c%i==0):
        nums += 1
        prime_check = 0
        print(i)

print(nums+prime_check)
