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
sys.setrecursionlimit(10**9)
from collections import defaultdict

t = int(input())

for _ in range(t):
    n,a,b,c,d = map(int,input().split())
    dic = defaultdict(int)
    dic[0] = 0
    dic[1] = d

    def calc(x):
        if(x==0):
            return 0
        if(dic[x] != 0):
            return dic[x]

        tmp = x*d
        if(x%2==0):
            tmp = min(tmp, calc(x//2) + a)
        else:
            tmp = min(tmp, calc(x//2) + a + d, calc(x//2 + 1) + a + d)
        if(x%3==0):
            tmp = min(tmp, calc(x//3) + b)
        elif(x%3==1):
            tmp = min(tmp, calc(x//3) + b + d)
        else:
            tmp = min(tmp, calc(1 + x//3) + b + d)
        if(x%5==0):
            tmp = min(tmp, calc(x//5) + c)
        elif(x%5 < 3):
            tmp = min(tmp, calc(x//5) + c + d*(x%5))
        else:
            tmp = min(tmp, calc(1 + x//5) + c + d*(5 - x%5))

        dic[x] = tmp
        return tmp

    print(calc(n))
