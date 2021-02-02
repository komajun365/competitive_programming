# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

x = int(input())
num = 100
for i in range(1,10000):
    num = int(num*1.01)
    if(num >= x):
        print(i)
        exit()
