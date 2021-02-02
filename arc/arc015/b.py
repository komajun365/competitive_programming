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

n = int(readline())
t = list(map(float,read().split()))

ans = [0]*6
it = iter(t)
for M,m in zip(it,it):
    if(M >= float('35.0')):
        ans[0] += 1
    elif(M >= float('30.0')):
        ans[1] += 1
    elif(M >= float('25.0')):
        ans[2] += 1

    if(m >= float('25.0')):
        ans[3] += 1

    if(M >= float('0.0'))&(m < float('0.0')):
        ans[4] += 1

    if(M < float('0.0')):
        ans[5] += 1

print(' '.join(map(str,ans)))
