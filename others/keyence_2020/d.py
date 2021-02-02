import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


left = [0] * n
right = [0] * n

for i in range(n):
    if(i % 2 == 0):
        left[i] = a[i]
        right[i] = b[i]
    if(i % 2 == 1):
        left[i] = b[i]
        right[i] = a[i]

bigger = {}

for i in range(n):
    bigger[i] = []
    bigger[i+n] = []
    for j in range(n):
        if(i != j):
            if(left[i] <= right[j]):
                bigger[i].append(j+n)
            if(right[i] <= left[j]):
                bigger[i+n].append(j)

print(bigger)

len = [-1] * (2*n)

def calc_len(i):
    if(len[i] != -1):
        return len[i]

    temp = bigger[i]
    if( len(temp) == 0):
        len[i] = 0
        return 0
    max = 0
    for j in range(len(temp)):
        max = max(max, calc_len(j) + 1)
    len[i] = max
    return max

for i in range(n*2):
    calc_len(i)

print(len)
