import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,r = map(int,input().split())

if(n> 10):
    ans = r
else:
    ans = r + 100 * (10-n)

print(ans)
