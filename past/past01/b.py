# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = list(map(int, read().split()))

for i in range(1,n):
    num = a[i]-a[i-1]
    if(num > 0):
        print('up {}'.format(num))
    elif(num < 0):
        print('down {}'.format(num*-1))
    else:
        print('stay')
