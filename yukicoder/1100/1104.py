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
a,b,c = map(int,input().split())
mod = 10**9 + 7

n -= 2
a,b,c = a-b,b-c,c-a

k = n//6
l = n%6

k_mul = pow(-27,k,mod)
a = (a*k_mul)%mod
b = (b*k_mul)%mod
c = (c*k_mul)%mod

for _ in range(l):
    a,b,c = a-b,b-c,c-a

print(' '.join(map(lambda x: str(x%mod),[a,b,c])))


# for i in range(30):
#     print(a,b,c)
#     a,b,c = a-b,b-c,c-a

'''
a2 = a1-b1
b2 = b1-c1
c2 = c1-a1

a3 = a-2b+c
b3 = b-2c+a
c3 = c-2a+b

a4 = -3b+3c
b4 = -3c+3a
c4 = -3a+3b

a5 = -3a-3b+6c
b5 = -3b-3c+6a
c5 = -3c-3a+6b

a6 = -9a+9c
b6 = -9b+9a
a6 = -9c+9b

a7 = -18a+9b+9c
b7 = -18b+9c+9a
c7 = -18c+9a+9b

a8 = -27a+27b
b8 = -27b+27c
c8 = -27c+27a

a2 - a8 で　-27倍になってる。これでいきましょう。

'''
