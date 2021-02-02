import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

h,w = map(int, input().split())
if(h==1)|(w==1):
    print(1)
    exit()

print((h*w + 1)//2)
