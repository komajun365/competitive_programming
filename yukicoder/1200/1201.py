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
m = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
mod = 1_000_000_007

ans = 0
for a in A:
    if(a==0):
        continue
    for b in B:
        gcd_num = gcd(a,b)
        ans += (a*(b+1))%mod - (b-gcd_num)
        ans %= mod

print(ans)
