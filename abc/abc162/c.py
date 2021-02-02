# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

k = int(input())
from math import gcd

ans = 0
for i in range(1, k+1):
    for j in range(1, k+1):
        for l in range(1, k+1):
            ans += gcd(i,gcd(j,l))

print(ans)
