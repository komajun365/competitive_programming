# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
a = list(map(int,input().split()))
f = list(map(int,input().split()))

lim = sum(a) -k
if(lim <= 0):
    print(0)
    exit()

min_ = 0
max_ = 10**12+1

a.sort()
a = tuple(a)
f.sort(reverse=True)
f = tuple(f)

for i in range(100):
    tmp = (max_ + min_)//2
    tmp_sum = 0
    for j in range(n):
        tmp_sum += max(0, a[j] - tmp//f[j])

    if(tmp_sum <= k):
        max_ = tmp
    else:
        min_ = tmp

    if(max_ - min_ == 1):
        break

print(max_)
