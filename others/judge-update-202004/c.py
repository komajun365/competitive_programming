# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import itertools

a = list(map(int,input().split()))

n = sum(a)
l = list(range(1,n+1))
p = itertools.permutations(l, n)

ans = 0
for i in p:
    boxes = [[999] * 4 for _ in range(4)]
    pointer = 0
    for j,val in enumerate(a):
        for k in range(val):
            boxes[j][k] = i[pointer]
            pointer += 1

    check = 1
    for j in range(3):
        for k in range(3):
            if(boxes[j][k] > boxes[j][k+1])|(boxes[j][k] > boxes[j+1][k]):
                check=0

    ans += check

print(ans)
