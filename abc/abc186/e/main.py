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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from math import gcd

t,*nsk = map(int,read().split())

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

ans = []
it = iter(nsk)
for n,s,k in zip(it,it,it):
    g = gcd(gcd(n,s),k)
    n //= g
    s //= g
    k //= g
    if(gcd(n,k) != 1):
        ans.append(-1)
        continue

    rev = modinv(k, n)
    if(rev == -1):
        ans.append(-1)
        continue
    x = (-s * rev) % n
    ans.append(x)
print('\n'.join(map(str,ans)))