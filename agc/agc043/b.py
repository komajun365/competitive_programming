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
a = input()

fac2 = [0] * (n+1)
i = 2
while(i <= n ):
    for j in range(i,n+1,i):
        fac2[j] += 1
    i *= 2

for i in range(1,n+1):
    fac2[i] += fac2[i-1]

def calc(x):
    len_x = len(x)
    res = 0
    for i,xi in enumerate(x):
        if(fac2[len_x-1] - fac2[len_x-1-i] - fac2[i] > 0):
            continue
        res = res ^ xi
    return res

if(a.count('2')==0):
    x = []
    for ai in a:
        x.append(int(ai)//2)
    res = calc(x)
    if(res==0):
        print(0)
    else:
        print(2)
else:
    x = []
    for ai in a:
        x.append( (int(ai)-1) % 2)
    res = calc(x)
    print(res)
