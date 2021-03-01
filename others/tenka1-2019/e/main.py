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

import sys
read = sys.stdin.buffer.read
from math import gcd

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

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5//1)+1 ):
        if(temp%i == 0):
            count=0
            while( temp%i == 0):
                count += 1
                temp = temp // i
            arr.append([i, count])

    if(temp != 1):
        arr.append([temp, 1])

    if(arr == []) and n != 1:
        arr.append([n, 1])

    return arr

n,*a = map(int,read().split())

primes = sieve(n+3)
gcd_num = a[0]
for ai in a:
    gcd_num = gcd(gcd_num,ai)

ans = set()

for i,cnt in factorization(gcd_num):
    ans.add(i)

for p in primes:
    if a[-1] % p != 0:
        continue
    for i in range(p-1):
        tot = sum( a[i:n:p-1] )
        if tot % p != 0:
            break
    else:
        ans.add(p)

ans = list(ans)
ans.sort()

print('\n'.join(map(str,ans)))

