# import math
# import numpy as np

# n, m = 4,4
# a_list = np.array([1,9,3,5])
n = int(input())
s = input()

ct = 0
ct_max = 0
for i in range(1,n):
    if(ct_max >= n-i)

    forward = s[:n-i]
    back = s[i:]
    for j in range(n-i):
        f = forward[j]
        b = back[j]
        if(f==b):
            ct += 1
            if(ct_max < ct):
                ct_max = ct*1
            if(ct_max >= i):
                break()
        else:
            ct = 0

print(ct_max)
