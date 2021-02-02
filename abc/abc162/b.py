# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
ans = 0
for i in range(1,n+1):
    if(i%3 != 0)&(i%5 != 0):
        ans += i

print(ans)
