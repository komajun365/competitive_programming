# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b,k = map(int,input().split())
a_ = max(0, a-k)
b_ = max(0, b - max(k-a, 0))
print('{} {}'.format(a_,b_))
