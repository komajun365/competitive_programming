# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
a = list(map(int,input().split()))
if(sum(a) > n):
    print(-1)
else:
    print(n-sum(a))
