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

t,*ab = map(int, read().split())

def calc(a,b):
    res = []
    if(a^b < a):
        length = 0
        for i in range(60):
            if (1<<i) > b:
                length = i
                break
        for i in range(length-1,0,-1):
            if(a&b) >> i :
                a -= (1<<i)
                b -= (1<<i)
            elif(a>>i)!=(b>>i):
                break
            if(a==0):
                a += (1<<i)
                b += (1<<i)
                break
    r_bit = 0
    while((a^b) > a):
        if(a & (1 << r_bit)):
            res.append(1 << r_bit)
            a += (1 << r_bit)
        r_bit += 1
    res2 = []
    for i in range(60):
        if(b^(1<<i) < (1<<i)):
            break
        if (b>>i)&1 :
            res2.append(1<<i)
    res += res2[::-1]
    print(len(res))
    print(' '.join(map(str,res)))
    # return res

it = iter(ab)
for a,b in zip(it,it):
    calc(a,b)
