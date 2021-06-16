# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = [None] * n
for i in range(n):
    num = int(input())
    a[i] = [list(map(int,input().split())) for _ in range(num)]

def check(i, bit_):
    com = a[i]
    for xy in com:
        x,y = xy
        if( (bit_ >> (x-1))&1 != y ):
            return 0
    return 1

ans = 0
for i in range(2**n):
    c_num = 1
    honest = 0
    for j in range(n):
        if( (i>>j)&1 == 1 ):
            honest += 1
            c_num *= check(j, i)
    if(c_num == 0):
        continue

    ans = max(ans, honest)

print(ans)
