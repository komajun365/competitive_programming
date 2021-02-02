# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from math import gcd

n,q = map(int,input().split())
A = list(map(int,input().split()))
S = list(map(int,input().split()))

tmp = A[0]
a_zip = [(tmp,0)]
for i in range(1,n):
    if(tmp == 1):
        break
    a = A[i]
    tmp_next = gcd(tmp,a)
    if(tmp != tmp_next):
        tmp = tmp_next
        a_zip.append((tmp, i))

for s in S:
    for tmp in a_zip:
        a,i = tmp
        s = gcd(s,a)
        if(s == 1):
            print(i+1)
            break
    if(s!=1):
        print(s)
