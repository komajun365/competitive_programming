# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
ans = 0

def calc(n,k):
    while(n%k==0):
        n = n//k
    n  %= k
    return n

def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if(n%i == 0):
            divisors.append(i)
            if(i!= n//i):
                divisors.append(n//i)

    return  divisors

divisors = make_divisors(n)
divisors += make_divisors(n-1)
divisors = set(divisors)
for i in divisors:
    if(i != 1):
        if( calc(n,i)==1 ):
            ans += 1

print(ans)
