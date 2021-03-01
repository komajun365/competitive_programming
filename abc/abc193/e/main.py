# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read
from math import gcd

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

t,*case = map(int,read().split())
inf = 10**20

def calc(x,y,p,q):
    xy = (x + y)*2 
    pq = p + q
    res = inf
    gcd_0 = gcd(pq,xy)
    for i in range(1,y+q):
        i += x
        d = gcd(i,gcd_0)
        a,b,m = pq//d, i//d, xy//d
        if gcd(a,m) != 1:
            continue
        mi = modinv(a,m)
        if mi == -1:
            continue
        cyc = (mi * b) % m
        if cyc == 0:
            cyc = m

        tmp = cyc * pq - q
        for _ in range(q):
            if x <= (tmp % xy) < x+y:
                res = min(res,tmp)
                break
            tmp += 1
        # rem = tmp % xy
        # if not (x <= rem < x+y):
        #     tmp += (x - rem) % xy
        # if tmp <= cyc * pq - q:
        #     res = min(res,tmp)
        # print(x,y,p,q,i,tmp,cyc)
    return res

it = iter(case)
for x,y,p,q in zip(it,it,it,it):
    res = calc(x,y,p,q)
    if res == inf:
        print('infinity')
    else:
        print(res)
