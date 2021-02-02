import sys
import os
f = open('C:\\Users\\scare\\Documents\\git\\atcoder\\input.txt', 'r')
sys.stdin = f

###############################################

import numpy as np

n = int(input())
ls = list(map(int, input().split()))
ls.sort()

ans = 0

ab = np.zeros(2001)

ab[(ls[0] + ls[1])] += 1

for i in range(2,n):
    l_temp = ls[i]
    ans += sum(ab[l_temp+1:])

    for j in range(i):
        ab[( l_temp + ls[j] )] += 1

print(int(ans))
