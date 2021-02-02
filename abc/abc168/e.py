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
from collections import defaultdict
from math import gcd

n = int(readline())
data = list(map(int,read().split()))
mod = 1000000007

it = iter(data)
a_b = defaultdict(lambda :[0,0])
a0 = 0
b0 = 0
ab0 = 0
ans = 0
for a,b in zip(it,it):
    if(a==b==0):
        ab0 += 1
        continue
    if(a*b==0):
        if(a==0):
            a0 += 1
        if(b==0):
            b0 += 1
    else:
        if(a/b > 0):
            a = abs(a)
            b = abs(b)
            gcd_num = gcd(a,b)
            a_b[(a//gcd_num,b//gcd_num)][0] += 1
        else:
            a = abs(a)
            b = abs(b)
            gcd_num = gcd(a,b)
            a_b[(b//gcd_num,a//gcd_num)][1] += 1

exp2 = [1] * (n+1)
for i in range(n):
    exp2[i+1] = exp2[i] * 2
    exp2[i+1] %= mod


ans += (ans+1) * ( exp2[a0]-1  + exp2[b0]-1)
ans %= mod

for key,val in a_b.items():
    ans += (ans+1) * ( exp2[val[0]]-1  + exp2[val[1]]-1)
    ans %= mod

ans += ab0
ans %= mod

print(ans)
