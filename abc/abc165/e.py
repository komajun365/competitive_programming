# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
if(n%2==1):
    for i in range(1,m+1):
        print(' '.join(map(str,[i,n+1-i])))
    exit()

m1,m2 = (m+1)//2 ,m//2
sum1 = 1 + n//2
sum2 = (n//2+1) + (n-1)
for i in range(m1):
    print(' '.join(map(str,[1+i,n//2 -i])))
for i in range(m2):
    print(' '.join(map(str,[n//2+1+i,n-1-i])))
