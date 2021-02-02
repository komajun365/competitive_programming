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

h,w,n = map(int,input().split())
r,c =  map(int,input().split())
s = input()
t = input()

def check(m,p,l):
    left = 0
    right = l
    for si,ti in zip(s[::-1],t[::-1]):
        if(ti==m):
            right = min(right+1,l)
        elif(ti==p):
            left = max(left-1,0)

        if(si==m):
            left = left+1
        elif(si==p):
            right = right-1

        if(left==right):
            return (-1,-1)

    return (left+1,right+1)

left,right = check('L','R',w)
if(not left<=c<right):
    print('NO')
    exit()

left,right = check('U','D',h)
if(not left<=r<right):
    print('NO')
    exit()

print('YES')



'''
たて、よこ、それぞれ生き残れる場所を管理していけばよい？

oo
xo
oo

LDRL
LRR


'''
