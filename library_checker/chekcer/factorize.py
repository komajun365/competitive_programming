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

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5//1)+1 ):
        if(temp%i == 0):
            count=0
            while( temp%i == 0):
                count += 1
                temp = temp // i
            arr.append([i, count])
        if temp==1:
            break

    if(temp != 1):
        arr.append([temp, 1])
    
    return arr

import sys
read = sys.stdin.read

q,*a = map(int,read().split())

for ai in a:
    arr = factorization(ai)
    res = []
    res.append( sum([x[1] for x in arr]) )
    for x in arr:
        for i in range(x[1]):
            res.append(x[0])
    print(*res, sep=' ')
