# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

from math import gcd

n = int(input())
x = list(map(int,input().split()))

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

primes = sieve(50)
l = len(primes)

ans = 1
for pi in primes:
    ans *= pi
for i in range(1<<l):
    num = 1
    for j in range(l):
        if (i >> j) & 1:
            num *= primes[j]
    
    for xi in x:
        if xi == 1:
            continue
        if gcd(xi,num) == 1:
            break
    else:
        ans = min(ans,num)

print(ans)



# use = [0] * len(primes)

# for xi in x:
#     for i,p in enumerate(primes):
#         if xi % p == 0:
#             use[i] = 1

# ans = 1
# for i,p in enumerate(primes):
#     if use[i] == 1:
#         ans *= p

# print(ans)