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

# n = int(input())
# x = input()

memo = [-1] * (10000)
def calc(x):
    if(memo[x] != -1):
        return memo[x]
    if(x==0):
        return 0
    cnt = 0
    x2 = x
    while(x2 > 0):
        cnt += (x2&1)
        x2 //= 2
    next = x%cnt
    memo[x] = 1 + calc(next)
    return memo[x]

for i in range(20):
    print(i, calc(i))
