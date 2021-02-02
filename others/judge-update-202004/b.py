# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
balls = {'R':[], 'B':[]}
for i in range(n):
    x,c = input().split()
    balls[c].append(int(x))

for tmp in [balls['R'],balls['B']]:
    tmp.sort()
    for i in tmp:
        print(i)
