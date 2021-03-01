# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
for i in range(1,10):
    for j in range(1,10):
        if(n == i*j):
            print('Yes')
            exit()

print('No')
