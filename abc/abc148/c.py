# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b = map(int,input().split())
from fractions import gcd
ans = a*b//gcd(a,b)
print(ans)
