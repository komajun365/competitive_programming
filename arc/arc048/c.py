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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from math import gcd

n = int(readline())
l = list(map(int,read().split()))
mod = 10**9+7

l.sort()
base = l[0]
ans = pow(2,base,mod)

if(n==1):
    print(ans)
    exit()

gcd_num = l[1]-base
for li in l[1:]:
    gcd_num = gcd(gcd_num,li-base)

ans *= pow(2, (gcd_num+1)//2 ,mod)
ans %= mod
print(ans)




'''
00,0000,00000000
00,00

aa,aabb,aabbbbbb


'''
