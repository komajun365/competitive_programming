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

from math import gcd

n = int(input())
a = list(map(int,input().split()))

def print_result(x):
    if(x==0):
        print('First')
    else:
        print('Second')
    exit()

if(n == 1):
    print_result(a[0]%2)

cnt = 0
while(True):
    tot = sum(a)
    if(min(a) == 1):
        print_result( (tot-n+cnt+1)%2 )
    if (tot-n)%2==1 :
        print_result(cnt%2)
    if(tot == n):
        print_result((cnt+1)%2)

    minus = 0
    g = a[0]
    if(g%2==1):
        minus += 1
        g -= 1
    for ai in a[1:]:
        if(ai%2 == 1):
            minus += 1
            ai -= 1
        g = gcd(g,ai)

    if(minus != 1)|(g==1):
        print_result((cnt+1)%2)

    for i in range(n):
        a[i] //= g
    cnt += 1
