# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int,input().split()))
ai = [(val, ind) for ind,val in enumerate(a)]
ai.sort()

left = 0
right = n-1
ans = 0
skip = False
for val,ind in ai:
    len_l = abs(ind-left)
    len_r = abs(ind-right)
    if(skip):
        ans += max(len_l, len_r) * val
        len_l += 1
        len_r += 1
        skip = False
        continue

    if(len_l > len_r):
        ans += val * len_l
        left +- 1
    elif(len_l < len_r):
        ans += val * len_r
        right -= 1
    else:
        ans += val * len_l
        skip = True

print(ans)
