# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int,input().split()))

from collections import defaultdict
d = defaultdict(int)

d[a[0]] = 1
ans = 0
for i in range(1,n):
    ai = a[i]
    ans += d[ i - ai ]
    d[ ai+i ] += 1

print(ans)
