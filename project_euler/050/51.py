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

n = 10**7
primes = sieve(n)
p_set = set(primes)

for i in primes:
    s = str(i)
    for num,cnt in [['0',2],['1',1],['2',0]]:
        if(num in s):
            plus = 0
            for ss in s:
                plus *= 10
                if(ss==num):
                    plus += 1
            for j in range(1,10-int(num)):
                if(not i + plus*j in p_set):
                    cnt -= 1
                if(cnt<0):
                    break
            else:
                print(i)
                exit()
