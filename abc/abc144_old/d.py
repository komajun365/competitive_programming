# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b,x = map(int,input().split())
import math

if( x*2 < a*a*b):
    tan_y = 2*x/(b*b*a)
    ans = 90 - math.degrees(math.atan(tan_y))

else:
    tan_x = 2*(a*a*b - x)/(a*a*a)
    ans = math.degrees(math.atan(tan_x))

print(ans)
