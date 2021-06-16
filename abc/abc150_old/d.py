import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import fractions

n, m  = map(int, input().split())
a = list(map(int, input().split()))

exp2 = 0
temp = a[0]
while(True):
    if(temp%2 == 1):
        break
    exp2 += 1
    temp /= 2

a_div = []
for i in range(n):
    if(a[i] % 2**exp2 != 0):
        print(0)
        exit()
    if( a[i] % (2**(exp2+1)) == 0):
        print(0)
        exit()

    a_div.append(a[i]//(2**exp2))

lcm = a_div[0]
for i in range(1, n):
    lcm = lcm * a_div[i] // fractions.gcd(lcm, a_div[i])

base = lcm * 2**(exp2 -1)

print( ((m // base) + 1)//2 )
