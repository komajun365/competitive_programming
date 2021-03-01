# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())

ans = n-1
for i in range(2,10**6+1):
    if(n%i == 0):
        ans = min(ans, i + n//i - 2)

print(ans)
