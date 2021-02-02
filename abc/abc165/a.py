# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

k = int(input())
a,b = map(int,input().split())
for i in range(a,b+1):
    if(i%k==0):
        print('OK')
        exit()
print('NG')
