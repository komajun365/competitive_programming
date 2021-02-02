# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int,input().split()))

child =  [0] * (n+1)
for i in a:
    child[i] += 1

for i in child[1:]:
    print(i)
    
