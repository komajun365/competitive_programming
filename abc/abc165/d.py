# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b,n = map(int,input().split())
if( n >= b):
    x = b-1
else:
    x = n

ans = int( a*(x/b - int(x/b) ) )
print(ans)
