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
w1 = input()
words = set()
words.add(w1)
for i in range(1,n):
    w2 = input()
    if(w2 in words)|(w1[-1] != w2[0]):
        if(i%2==0):
            print('LOSE')
        else:
            print('WIN')
        exit()
    words.add(w2)
    w1 = w2

print('DRAW')
