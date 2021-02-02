import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import numpy as np

n, d, a  = map(int,input().split())
x = []
h = []
for i in range(n):
    x_temp,h_temp = map(int,input().split())
    x.append(x_temp)
    h.append(h_temp)

x = np.array(x, dtype=np.int64)
h = np.array(h, dtype=np.int64)
sort_ind = np.argsort(x)
x = x[sort_ind]
h = h[sort_ind]

ans = 0
for i in range(n):
    if (h[i] <= 0):
        continue
    at_num = ((h[i] -1 )// a) + 1
    ans += at_num
    h[i] -= at_num * a
    x_origin = x[i]
    while(True):
        i += 1
        if(i >= n):
            break
        if(x_origin + 2*d >= x[i]):
            h[i] -= at_num * a
        else:
            break

print(ans)
