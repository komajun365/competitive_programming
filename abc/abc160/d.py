# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,x,y = map(int,input().split())
left = x-1
mid = y-x+1
right = n-y

x_to_mid = [0] * n
x_to_mid[0] = 1
for i in range(1, mid//2):
    x_to_mid[i] = 2
x_to_mid[mid//2] = 1 + mid%2

ans = [0] * n
#LL,RR
for i in [left,right]:
    for j in range(1,i):
        ans[j] += i-j

#mid-mid
for i in range(1, 1 + mid//2):
    ans[i] += mid * x_to_mid[i] // 2

#LR
for i in range(left):
    for j in range(right):
        ans[i+j+3] += 1

#L-mid,R-mid
for i in [left,right]:
    for j in range(n):
        tmp = x_to_mid[j]
        if(tmp==0):
            break
        for k in range(1,i+1):
            ans[ j+k ] += tmp

for i in ans[1:]:
    print(i)
