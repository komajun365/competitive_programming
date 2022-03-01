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

def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if(n%i == 0):
            divisors.append(i)
            if(i!= n//i):
                divisors.append(n//i)

    return  divisors

n,*ab = map(int,read().split())
a = ab[::2]
b = ab[1::2]
div_a = make_divisors(a[0])
div_b = make_divisors(b[0])
div_a.sort()
div_b.sort()

h = len(div_a)
w = len(div_b)

encode_a = dict()
for i in range(h):
    encode_a[div_a[i]] = i
encode_b = dict()
for i in range(w):
    encode_b[div_b[i]] = i

dp = [[0] * w for _ in range(h)]
dp[-1][-1] = 1

for i in range(1,n):
    ai,bi = ab[i*2:i*2+2]
    dp2 = [[0] * w for _ in range(h)]
    for j in range(h):
        for k in range(w):
            if dp[j][k] == 1:
                j1 = encode_a[gcd(div_a[j],ai)]
                k1 = encode_b[gcd(div_b[k],bi)]
                dp2[j1][k1] = 1
                j2 = encode_a[gcd(div_a[j],bi)]
                k2 = encode_b[gcd(div_b[k],ai)]
                dp2[j2][k2] = 1
    dp,dp2 = dp2,dp

ans = 1
for j in range(h):
    for k in range(w):
        if dp[j][k] == 1:
            ans = max(ans, div_a[j] * div_b[k] // gcd(div_a[j],div_b[k]))
print(ans)