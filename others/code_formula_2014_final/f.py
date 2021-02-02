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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from math import gcd

n = int(readline())
b = list(map(int,read().split()))

if(n==1):
    print(0)
    exit()
elif(n==2):
    if(b[0]==b[1]):
        ans = 0
    else:
        ans = 1
    print(ans)
    exit()

b += b

ans = n
for i in range(3):
    tmp = 0
    j = i
    while(j < i+n):
        x,y,z = b[j:j+3]
        g = gcd(x,z)
        if(y%g!=0):
            tmp += 1
            j += 2
        j += 1

    ans = min(ans,tmp)

print(ans)
print(b)
