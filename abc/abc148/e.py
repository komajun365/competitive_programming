# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
if(n%2==1):
    print(0)
    exit()
n = n//2
ans = 0
while(n>0):
    ans += n//5
    n = n//5
print(ans)
