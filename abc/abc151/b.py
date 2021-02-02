import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k,m = map(int, input().split())
a = list(map(int, input().split()))

ans = n*m - sum(a)

if(ans > k):
    print(-1)
else:
    print(max(0,ans))
