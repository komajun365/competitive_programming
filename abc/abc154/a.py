import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s,t = input().split()
a,b = map(int, input().split())
u = input()

if(s==u):
    a -= 1
if(t==u):
    b -= 1

print('{} {}'.format(a,b))
