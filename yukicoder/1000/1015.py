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

n,x,y,z = map(int,input().split())
a = list(map(int,input().split()))

cnt_10000 = 0
rem = [0]*10
for i in range(n):
    cnt_10000 += a[i]//10000
    a[i] %= 10000
    rem[a[i]//1000] += 1

if(cnt_10000 <= z):
    z -= cnt_10000
    cnt_10000 = 0
else:
    cnt_10000 -= z
    z = 0

cnt_10000 *= 10
if(cnt_10000 <= y*5):
    y -= cnt_10000//5
    cnt_10000 = 0
else:
    cnt_10000 -= y*5
    y = 0

if(cnt_10000 <= x):
    x -= cnt_10000
    cnt_10000 = 0
else:
    print('No')
    exit()

if(sum(rem) <= z):
    print('Yes')
    exit()


for i in range(9,-1,-1):
    if(rem[i] >= z):
        rem[i] -= z
        z = 0
        break
    z -= rem[i]
    rem[i] = 0

for i in range(9,4,-1):
    if(rem[i] >= y):
        rem[i-5] += y
        rem[i] -= y
        y = 0
        break
    rem[i-5] += rem[i]
    y -= rem[i]
    rem[i] = 0

if(sum(rem) <= y):
    print('Yes')
    exit()

for i in range(4,-1,-1):
    if(rem[i] >= y):
        rem[i] -= y
        y = 0
        break
    y -= rem[i]
    rem[i] = 0

need = 0
for i,ri in enumerate(rem,1):
    need += ri*i

if(need <= x):
    print('Yes')
else:
    print('No')
