import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int, input().split())

ans = 1
while(n >= k):
    n = n//k
    ans += 1

print(ans)
