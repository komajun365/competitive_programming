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

1+1+1+2+k = 1*1*1*2*k
という感じで積和数は作れるので、kの最小積和数は2k以下。

素数でない数xを与えられたときに、
x1*x2の形に分解する。
(x1の積和数の形)*x2*(x-x1-x2個の1)　で積和数が作れる。
これをカウントしていけば、xの積和数としての集合の大きさの候補がメモれる。

24000までで約数の数が最大なのは20160で84個。

みたいな方針？
'''

n = 12000

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

primes = sieve(n*2)
p_set = set(primes)

def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if(n%i == 0):
            divisors.append(i)
            if(i!= n//i):
                divisors.append(n//i)

    return  divisors


ans = set()

remain = set(range(2,n+1))
# print(remain)

size = [set() for _ in range(n*2 + 1)]
size[1].add(1)
i=2
while (remain):
    # print(i)
    if(i in primes):
        i += 1
        continue

    for p in range(2,int(i**0.5)+1):
        if(i%p==0):
            ones = i-p-i//p
            size[i].add(ones + 2)
            for j in size[i//p]:
                size[i].add(ones + j + 1)

    for j in size[i]:
        if(j in remain):
            remain.remove(j)
            ans.add(i)

    i+=1

print(sum(ans))

# for i,j in enumerate(size):
#     print(i,j)
#
# print(ans)
# print(remain)


'''
k=10



'''
