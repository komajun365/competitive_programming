import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
h = list(map(int,input().split()))

if ( n <= k):
    print(0)
else: 
    h = sorted(h)
    h = h[:(n-k)]

    print(sum(h))
