import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

k , x = map(int, input().split())

if(k* 500 >= x):
    print('Yes')
else:
    print('No')
