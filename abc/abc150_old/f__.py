import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_30 = [0]*30
b_30 = [0]*30
n_1 = 0
for i in range(n):
    n_1 += 1 << i
    for j in range(30):
        a_30[j] +=  (a[i] & 2**j) >> j << i
        b_30[j] +=  (b[i] & 2**j) >> j << i



for k in range(n):
    x = 0
    check=True
    for j in range(30):
        a_temp  = a_30[j]
        a_30[j] = (a_temp >> 1) + ((a_temp & 1) << (n-1))
        if( (a_temp ^ b_30[j]) == n_1 ):
            x += (1 << j)
        elif( a_temp ^ b_30[j] != 0 ):
            check=False
    if(check):
        print('{} {}'.format(k, x))
