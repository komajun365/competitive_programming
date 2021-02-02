# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import math

a,b = map(int,readline().split())
n = int(readline())
cd = list(map(int,read().split()))
if(a>b):
    a,b = b,a

diag = (a**2+b**2)**0.5
theta = math.atan(a/b)

def check(c,d):
    if(c > diag):
        phi = math.pi/2 - theta
    else:
        phi = math.asin(c/diag) - theta

    if(phi < theta):
        return False

    width = diag * math.cos(phi-theta)
    if(d > width):
        return True
    else:
        return False

ans = []
it = iter(cd)
for c,d in zip(it,it):
    if(c>d):
        c,d = d,c

    if(a<c)&(b<d):
        ans.append('YES')
        continue


    if(check(c,d))|(check(d,c)):
        ans.append('YES')
        continue

    ans.append('NO')

print('\n'.join(ans))
