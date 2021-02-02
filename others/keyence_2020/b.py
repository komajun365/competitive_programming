import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import numpy as np

n = int(input())

left = np.zeros(n)
right = np.zeros(n)
for i in range(n):
    x, l = map(int, input().split())
    left[i] = int(x-l)
    right[i] = int(x+l)

sort_ind = np.argsort(right)
left = left[sort_ind]
right = right[sort_ind]

ans = 0
right_now = -1 * 10**10
for i in range(n):
    if(left[i] >= right_now):
        ans += 1
        right_now = right[i]

print(ans)
