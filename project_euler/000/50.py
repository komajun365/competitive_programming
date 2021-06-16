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


pl = sieve(10**6)
ps = set(pl)

ans = 0
longest = 0
l = len(pl)
for i in range(l-1):
    x = pl[i]
    for j in range(i+1,l):
        x += pl[j]
        if x > 10**6:
            break
        if x in ps:
            if longest < j-i+1:
                ans = x
                longest = j-i+1
                print(ans,longest)



















