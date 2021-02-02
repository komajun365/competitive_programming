# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b,x = map(int,input().split())

def calc(n):
    ans = a*n + b * len(str(n))
    return ans

if(calc(1) > x):
    print(0)
    exit()
elif(calc(10**9) <= x):
    print(10**9)
    exit()


min_ = 1
max_ = 10**9

for _ in range(50):
    tmp = (min_ + max_)//2
    tmp_c = calc(tmp)
    if(tmp_c <= x):
        min_ = tmp
    else:
        max_ = tmp

    if(max_ - min_ == 1):
        break

print(min_)
