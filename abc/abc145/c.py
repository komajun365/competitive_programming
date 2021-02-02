# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        x1,y1 = xy[i]
        x2,y2 = xy[j]
        ans += ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print(ans*(2/n))
