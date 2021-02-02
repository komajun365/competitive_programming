import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b,m = map(int,input().split())
a_s = list(map(int,input().split()))
b_s = list(map(int,input().split()))
xyc = [list(map(int,input().split())) for _ in range(m)]

ans = min(a_s) + min(b_s)
for tmp in xyc:
    x,y,c = tmp
    ans = min(ans, a_s[x-1] + b_s[y-1] - c)

print(ans)
