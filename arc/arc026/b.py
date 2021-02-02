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

n = int(input())
if(n==1):
    print('Deficient')
    exit()

tot = 1
for i in range(2,n):
    if(i**2 > n):
        break
    if(n%i==0):
        tot += i + n//i
        if(i**2 == n):
            tot -= i

if(tot==n):
    print('Perfect')
elif(tot>n):
    print('Abundant')
else:
    print('Deficient')
