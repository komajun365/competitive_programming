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

def calc_pm(p):
    m = p**2-p
    pm_m = p-1
    pm_c = (p-1).bit_length()-1
    return m,pm_c,pm_m

for i in range(2,100):
    m,pm_c,pm_m = calc_pm(2**i - 1)
    if(pm_c*12345 < pm_m):
        print(i)
        print(m,pm_c,pm_m)
        break

p = pm_c*12345+1
a,b,c = calc_pm(p)
print(calc_pm(p))
print(b*12345 < c)


print(calc_pm(5))
'''
4^tと2^tが整数なので、

p^2=p+k (2<=p)
となる。
perfectな条件は、
2^q=p (qは整数)

二分探索すればOK。

'''
