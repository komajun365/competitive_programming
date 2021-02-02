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

n,k = map(int,readline().split())
ab = list(map(int,read().split()))

target = [k]
for i in range(1,30):
    if((k>>i)&1):
        target.append(( k-(1<<i)) | ((1<<i)-1) )

ans = 0
for i in target:
    val = 0
    it = iter(ab)
    for a,b in zip(it,it):
        if( a - (i&a) == 0 ):
            val += b
    ans = max(ans,val)

print(ans)
# print(target)

'''
10010010011
01111111111
10001111111
10010001111
10010010001

101100
011111
100111
101011


a=1110
b=1010

a&b = 1010
a|b = 1110

'''
