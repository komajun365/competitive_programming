# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = tuple(map(int,input().split()))

if(n <= 3):
    print(max(a))
    exit()

left = [0] * (n+1)
right = [0] * (n+1)

left[1] = a[0]
left[2] = max(a[0],a[1])
for i in range(3,n+1):
    if(i%2==0):
        left[i]  = max(left[i-3] + max(a[i-2], a[i-1]),
                        left[i-2] + a[i-1])
    else:
        left[i] = left[i-2] + a[i-1]

right[-2] = a[-1]
right[-3] = max(a[-1],a[-2])
for i in range(n-3,-1,-1):
    if((n-i)%2==0):
        right[i]  = max(right[i+3] + max(a[i+1], a[i]),
                        right[i+2] + a[i])
    else:
        right[i] = right[i+2] + a[i]

ans = left[-2]
for i in range(0,n-1 ):
    ans = max(ans, left[i] + right[i+2])

if(n%2==0):
    print(left[-1])
else:
    print(ans)
