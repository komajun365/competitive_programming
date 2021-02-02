# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
s = input()

r = s.count('R')
g = s.count('G')
b = s.count('B')

ans = r*g*b

for i in range(1,n//2 + 10):
    for j in range(n):
        if(j + i*2 >= n):
            break
        a,b,c = s[j],s[j+i],s[j+i*2]
        if(a!=b)&(b!=c)&(a!=c):
            ans -= 1

print(ans)
