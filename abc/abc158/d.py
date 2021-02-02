import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
q = int(input())

import sys
input = sys.stdin.readline

qs = [list(input().split()) for _ in range(q)]

left = ''
right = ''


front = False
for i in qs:
    if(i[0] == '1'):
        front = not front
        continue

    f = int(i[1])
    c = i[2]
    if(front + f == 2):
        right = right + c
    else:
        left = left + c

if(not front):
    ans = left[::-1] + s + right
else:
    ans = right[::-1] + s[::-1] + left

print(ans)
