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

n = int(input())
a = list(map(int,input().split()))

tot = sum(a)
cyc = tot// (n*(n+1)//2)
if(cyc == 0):
    print('NO')
    exit()
if( tot % cyc != 0):
    print('NO')
    exit()

cnt = 0
for i in range(n):
    tmp = a[i]-a[i-1]-cyc
    if(tmp%n != 0):
        print('NO')
        exit()
    cnt += abs(tmp//n)

if(cnt == cyc):
    print('YES')
else:
    print('NO')
