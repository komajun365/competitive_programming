# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int,input().split()))

a_l = a[:n]
a_c = a[n:2*n]
a_r = [ -1*i for i in  a[2*n:]]

left = [0] * (n+1)
right = [0] * (n+1)

# ヒープキュー（最小値・最大値の取得）
from heapq import heapify,heappop,heappush

left[0] = sum(a_l)
heapify(a_l)
for i,val in enumerate(a_c):
    heappush(a_l,val)
    left[i+1] = left[i] + val - heappop(a_l)

right[-1] = -1 * sum(a_r)
heapify(a_r)
for i,val in enumerate(a_c[::-1],1):
    heappush(a_r,val * -1)
    right[n-i] = right[n+1-i] + val + heappop(a_r)

lr = [i-j for i,j in zip(left,right)]
print(max(lr))
