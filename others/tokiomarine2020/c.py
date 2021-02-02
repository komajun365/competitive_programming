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
a = list(map(int,read().split()))

def update(a):
    b = [0]*n
    for ind,i in enumerate(a):
        left = max(0,ind-i)
        right = ind+i+1
        b[left] += 1
        if(right<n):
            b[right] -= 1

    for i in range(1,n):
        b[i] += b[i-1]

    return b

for i in range(k):
    a = update(a)
    if(sum(a) == n*n):
        break

print(' '.join(map(str,a)))

# x = [0] * 1000
# x[0] = 1
# print(' '.join(map(str,x)))
