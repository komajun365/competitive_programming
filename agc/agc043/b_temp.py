import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import random
base = [0,1,2]

def calc(a):
    if(len(a) == 1):
        return a[0]

    tmp = abs(a[0] - a[-1])
    if( tmp < 2):
        return tmp
    else:
        if(calc(a[1:-1]) == 1):
            return 0
        else:
            return 2

for j in range(100):
    a = random.choices(base, k=9)
    a_t = a[:]
    # print(a)
    a_c = calc(a)

    while(len(a) > 1):
        tmp = []
        for i in range(len(a)-1):
            tmp.append(abs(a[i] - a[i+1]))
        a = tmp[:]

    if(a[0] != a_c):
        print(a_t)
        print(a_c)
        print(a[0])
